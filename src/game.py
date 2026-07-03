import pygame
import time
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, TICK_RATE, SLEEP_TIME
from src.hud import HUD
from src.background import Background
from src.entities import Player, Hazard

class Game:
    def __init__(self):

        """
        Função que inicializa o pygame, define a resolução da tela e desabilita o mouse
        """

        self.run = True
        self.clock = pygame.time.Clock()

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.mouse.set_visible(False)
        pygame.display.set_caption('Viagem Espacial')

        self.background = Background()
        self.hud = HUD()
        self.player = Player()
        self.hazard = Hazard()
        self.last_direction = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.last_direction = -1

                if event.key == pygame.K_RIGHT:
                    self.last_direction = 1

    def get_player_direction(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]

        if left and right:
            return self.last_direction
        if left:
            return -1
        if right:
            return 1
        return 0

    def reset(self):
        self.player.reset()
        self.hazard.reset()

    def loop(self):
        """
        Laço principal
        """

        while self.run:
            self.clock.tick(TICK_RATE)
            self.handle_events()

            # move o plano de fundo
            self.background.move(self.screen)

            # move e exibe o jogador de acordo com a direção selecionada
            direction = self.get_player_direction()
            self.player.move(direction)
            self.player.draw(self.screen)

            # exibe a pontuação
            self.hud.print_score(self.screen)

            # teste de colisão com a borda
            if self.player.collided_with_border():
                self.hud.print_collided_text(self.screen)
                self.hud.reset_score()
                pygame.display.update()
                time.sleep(SLEEP_TIME)
                self.reset()
                continue

            # move e exibe o hazard
            self.hazard.move()
            self.hazard.draw(self.screen)

            # teste de ultrapassagem do hazard
            if self.hazard.exited_screen():
                self.hazard.respawn()
                self.hud.increment_score()

            # teste de colisão entre player e hazard (game over)
            if self.hazard.collided(self.player):
                self.hud.print_lost_text(self.screen)
                pygame.display.update()
                time.sleep(SLEEP_TIME)
                self.run = False

            pygame.display.update()