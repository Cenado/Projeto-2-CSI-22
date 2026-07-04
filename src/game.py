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

        self._run = True
        self._clock = pygame.time.Clock()

        pygame.init()

        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.mouse.set_visible(False)
        pygame.display.set_caption('Viagem Espacial')

        self._background = Background()
        self._hud = HUD()
        self._player = Player()
        self._hazard = Hazard()
        self._last_direction = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._last_direction = -1

                if event.key == pygame.K_RIGHT:
                    self._last_direction = 1

    def get_player_direction(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]

        if left and right:
            return self._last_direction
        if left:
            return -1
        if right:
            return 1
        return 0

    def reset(self):
        self._player.reset()
        self._hazard.reset()

    def loop(self):
        """
        Laço principal
        """

        while self._run:
            self._clock.tick(TICK_RATE)
            self.handle_events()

            # move o plano de fundo
            self._background.move(self._screen)

            # move e exibe o jogador de acordo com a direção selecionada
            direction = self.get_player_direction()
            self._player.move(direction)
            self._player.draw(self._screen)

            # exibe a pontuação
            self._hud.print_score(self._screen)

            # teste de colisão com a borda
            if self._player.collided_with_border():
                self._hud.print_collided_text(self._screen)
                self._hud.reset_score()
                pygame.display.update()
                time.sleep(SLEEP_TIME)
                self.reset()
                continue

            # move e exibe o hazard
            self._hazard.move()
            self._hazard.draw(self._screen)

            # teste de ultrapassagem do hazard
            if self._hazard.exited_screen():
                self._hazard.respawn()
                self._hud.increment_score()

            # teste de colisão entre player e hazard (game over)
            if self._hazard.collided(self._player):
                self._hud.print_lost_text(self._screen)
                pygame.display.update()
                time.sleep(SLEEP_TIME)
                self._run = False

            pygame.display.update()