import pygame
import random
import time
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
    render_text_bateulateral = None
    render_text_perdeu = None

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

        # fontes
        my_font = pygame.font.Font("Fonts/Fonte4.ttf", 100)

        # Mensagens para o jogador
        self.render_text_bateulateral = my_font.render("COLISÃO!", 0,(255, 255, 255))  # ("texto", opaco/transparente 0/1, cor do texto)
        self.render_text_perdeu = my_font.render("GAME OVER!", 0, (255, 0, 0))  # ("texto, opaco/transparente 0/1, cor do texto)

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

    # Informa a quantidade de hazard que passaram e a Pontuação
    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, 35)
        passou = font.render("Passou: " + str(h_passou), True, (255, 255, 128))
        score = font.render("Score: " + str(score), True, (253, 231, 32))
        screen.blit(passou, (0, 50))
        screen.blit(score, (0, 100))
    #score_card()

    def loop(self):
        """
        Laço principal
        """
        score = 0
        h_passou = 0

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
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > 760 - 92 or x < 40 + 5:
                self.screen.blit(self.render_text_bateulateral, (80, 200))
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
                h_passou = h_passou + 1
                score = h_passou * 10

            # restrições para o game over
            if y < h_y + h_height:
                if x > h_x or x > h_x - 56:
                    if x < h_x + h_width or x < h_x - 56:
                        self.screen.blit(self.render_text_perdeu, (80, 200))
                        pygame.display.update()
                        time.sleep(3)
                        self.run = False

            # atualizando a tela
            pygame.display.update()

        # while self.run
    # loop()