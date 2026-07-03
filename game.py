import pygame
import random
import time
from hud import HUD
from background import Background
from entities import Player, Hazard

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None
    hazard = None
    render_text_bateulateral = None
    render_text_perdeu = None
    last_direction = 0

    def __init__(self, size, fullscreen):

        """
        Função que inicializa o pygame, define a resolução da tela,
        caption, e desabilita o mouse.
        """

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))  # tamanho da tela
        self.screen_size = self.screen.get_size()

        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Viagem Espacial')

        self.hud = HUD()

    # init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.last_direction = -1

                if event.key == pygame.K_RIGHT:
                    self.last_direction = 1
    # handle_events()

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
    # get_player_direction()

    def elements_update(self, dt):
        self.background.update(dt)
    # elements_update()

    def elements_draw(self):
        self.background.draw(self.screen)
    # elements_draw()

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.move (self.screen, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)
    # move_background()

    def loop(self):
        """
        Laço principal
        """

        # comprimento da margem
        margin_width = 60

        # Criar o Plano de fundo
        self.background = Background()

        # Criar entidades
        self.player = Player(self.width, self.height)
        self.hazard = Hazard(self.width, margin_width)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()

        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick(60)

            # Handle Input Events
            self.handle_events()

            # adiciona movimento ao background
            self.background.move(self.screen)

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            direction = self.get_player_direction()
            self.player.move(direction)

            # Mostrar Player
            self.player.draw(self.screen)

            # Mostrar score
            self.hud.print_score(self.screen)

            # Restrições do movimento do Player
            if self.player.collided_with_border(45, 758):
                self.hud.print_collided_text(self.screen)
                self.hud.reset_score()
                pygame.display.update()  # atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            self.hazard.move()
            self.hazard.draw(self.screen)

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo
            if self.hazard.exited_screen(self.height):
                self.hazard.respawn(self.width, margin_width)
                
                # determinando quantos hazard passaram e a pontuação
                self.hud.increment_score()

            # restrições para o game over
            if self.hazard.collided(self.player):
                self.hud.print_lost_text(self.screen)
                pygame.display.update()
                time.sleep(3)
                self.run = False

            # atualizando a tela
            pygame.display.update()

        # while self.run
    # loop()