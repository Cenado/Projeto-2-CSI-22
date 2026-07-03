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
    hazard_1 = hazard_2 = hazard_3 = hazard_4 = hazard_5 = None

    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0


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
        """
        Trata o evento e toma a ação necessária.
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            # se clicar em qualquer tecla, entra no if
            if event.type == pygame.KEYDOWN:
                # se clicar na seta da esquerda, anda 3 para a esquerda no eixo x
                if event.key == self.ESQUERDA:
                    self.mudar_x = -3
                # se clicar na seta da direita, anda 3 para a direita no eixo x
                if event.key == self.DIREITA:
                    self.mudar_x = 3

            # se soltar qualquer tecla, não faz nada
            if event.type == pygame.KEYUP:
                if event.key == self.ESQUERDA or event.key == self.DIREITA:
                    self.mudar_x = 0

    # handle_events()

    # Desenha o Player
    def draw_player (self, x, y):
        self.player.draw (self.screen, x, y)
    # draw_player()

    # Desenha Hazard
    def draw_hazard (self, hzrd, x, y):
        if hzrd == 0:
            self.hazard_1.draw(self.screen, x, y)
        elif hzrd == 1:
            self.hazard_2.draw(self.screen, x, y)
        elif hzrd == 2:
            self.hazard_3.draw(self.screen, x, y)
        elif hzrd == 3:
            self.hazard_4.draw(self.screen, x, y)
        elif hzrd == 4:
            self.hazard_5.draw(self.screen, x, y)
    # draw_hazard()

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.move (self.screen, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)
    # move_background()

    def loop(self):
        """
        Laço principal
        """

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_hazard = 7

        faixaA_x = 375
        faixaA_y = 0
        hzrd = 0
        h_x = random.randrange(125, 660)
        h_y = -500

        # Info Hazard
        h_width = 130 #55
        h_height = 130 #120

        # Criar o Plano de fundo
        self.background = Background()

        # Posicao do Player
        x = (self.width - 56) / 2
        y = self.height - 125

        # Criar o Player
        self.player = Player(x, y)

        # Criar Harzard_1
        self.hazard_1 = Hazard("Images/nave.png", h_x, h_y)

        # Criar Harzard_2
        self.hazard_2 = Hazard("Images/satelite.png", h_x, h_y)

        # Criar Harzard_3
        self.hazard_3 = Hazard("Images/cometa.png", h_x, h_y)

        # Criar Harzard_4
        self.hazard_4 = Hazard("Images/planeta.png", h_x, h_y)

        # Criar Harzard_5
        self.hazard_5 = Hazard("Images/ameaca.png", h_x, h_y)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 16

        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick(1000 / dt)

            # Handle Input Events
            self.handle_events()

            # adiciona movimento ao background
            self.background.move(self.screen)

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            x = x + self.mudar_x

            # Mostrar Player
            self.draw_player(x, y)

            # Mostrar score
            self.hud.print_score(self.screen)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > 760 - 92 or x < 40 + 5:
                self.hud.print_collided_text(self.screen)
                self.hud.reset_score()
                pygame.display.update()  # atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            h_y = h_y + velocidade_hazard / 4
            self.draw_hazard(hzrd, h_x, h_y)
            h_y = h_y + velocidade_hazard

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if h_y > self.height:
                h_y = 0 - h_height
                faixaA_y = 0
                h_x = random.randrange(125, 650 - h_height)
                hzrd = random.randint(0, 4)
                # determinando quantos hazard passaram e a pontuação
                self.hud.increment_score()

            # restrições para o game over
            if y < h_y + h_height:
                if x > h_x or x > h_x - 56:
                    if x < h_x + h_width or x < h_x - 56:
                        self.hud.print_lost_text(self.screen)
                        pygame.display.update()
                        time.sleep(3)
                        self.run = False

            # atualizando a tela
            pygame.display.update()

        # while self.run
    # loop()