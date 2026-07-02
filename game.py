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
    hazard = None
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

        # Lista de imagens de hazard
        self.hazard_images = [
            "Images/nave.png",
            "Images/satelite.png",
            "Images/cometa.png",
            "Images/planeta.png",
            "Images/ameaca.png"
        ]

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
        velocidade_background = 5
        velocidade_hazard = 7

        h_x = random.randrange(125, 660)
        h_y = -500

        # Info Hazard
        h_width = 130 #55
        h_height = 130 #120

        # movimento da margem esquerda
        movL_x = 0
        movL_y = 0

        # movimento da margem direita
        movR_x = 740
        movR_y = 0

        # Criar o Plano de fundo
        self.background = Background()

        # Posicao do Player
        x = (self.width - 56) / 2
        y = self.height - 125

        # Criar o Player
        self.player = Player(x, y)

        # Criar hazard
        self.hazard = Hazard(self.hazard_images[0], h_x, h_y)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 16

        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick(1000 / dt)

            # Handle Input Events
            self.handle_events()

            # Atualiza Elementos
            self.elements_update(dt)

            # Desenha o background buffer
            self.elements_draw()

            # adiciona movimento ao background

            self.move_background (movL_x, movL_y, movR_x, movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > 640 and movR_y > 640:
                movL_y -= 640
                movR_y -= 640

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            self.player.move(self.mudar_x)

            # Mostrar Player
            self.player.draw(self.screen)

            # Mostrar score
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if self.player.x > 760 - 92 or self.player.x < 40 + 5:
                self.screen.blit(self.render_text_bateulateral, (80, 200))
                pygame.display.update()  # atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            self.hazard.move(velocidade_hazard / 4)
            self.hazard.draw(self.screen)
            self.hazard.move(velocidade_hazard)

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo
            if self.hazard.y > self.height:
                self.hazard.respawn(
                    self.hazard_images[random.randint(0, 4)],
                    random.randrange(125, 650 - h_height),
                    -h_height)
                
                # determinando quantos hazard passaram e a pontuação
                h_passou = h_passou + 1
                score = h_passou * 10

            # restrições para o game over
            if self.player.y < self.hazard.y + h_height:
                if self.player.x > self.hazard.x - 56:
                    if self.player.x < self.hazard.x + h_width:
                        self.screen.blit(self.render_text_perdeu, (80, 200))
                        pygame.display.update()
                        time.sleep(3)
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()