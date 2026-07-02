import pygame

class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
    image = None
    margin_left = None
    margin_right = None

    def __init__(self):

        background_fig = pygame.image.load("Images/background.png")
        background_fig.convert()
        self.image = background_fig

        margin_left_fig = pygame.image.load("Images/margin_1.png")
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 600))
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 600))
        self.margin_right = margin_right_fig
    # __init__()

    def update(self, dt):
        pass
    # update()

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (740, 0))
    # draw()

    # Define posições do Plano de Fundo para criar o movimento
    def move (self, screen, movL_x, movL_y, movR_x, movR_y):

        #movimento background
        screen.blit(self.image, (movL_x, movL_y))
        screen.blit(self.image, (movL_x, movL_y + 600))
        screen.blit(self.image, (movL_x, movL_y + 1200))
        screen.blit(self.image, (movL_x, movL_y + 1800))
        screen.blit(self.image, (movL_x, movL_y + 2400))
        screen.blit(self.image, (movL_x, movL_y + 3000))
        screen.blit(self.image, (movL_x, movL_y - 600))
        screen.blit(self.image, (movL_x, movL_y - 1200))
        screen.blit(self.image, (movL_x, movL_y - 1800))
        screen.blit(self.image, (movL_x, movL_y - 2400))
        screen.blit(self.image, (movL_x, movL_y - 3000))
        screen.blit(self.image, (movL_x, movL_y - 3600))
        screen.blit(self.image, (movL_x, movL_y - 4200))
        screen.blit(self.image, (movL_x, movL_y - 4800))

        # movimento margem esquerda
        screen.blit(self.margin_left, (movL_x, movL_y))
        screen.blit(self.margin_left, (movL_x, movL_y + 600))
        screen.blit(self.margin_left, (movL_x, movL_y + 1200))
        screen.blit(self.margin_left, (movL_x, movL_y + 1800))
        screen.blit(self.margin_left, (movL_x, movL_y + 2400))
        screen.blit(self.margin_left, (movL_x, movL_y + 3000))
        screen.blit(self.margin_left, (movL_x, movL_y - 600))
        screen.blit(self.margin_left, (movL_x, movL_y - 1200))
        screen.blit(self.margin_left, (movL_x, movL_y - 1800))
        screen.blit(self.margin_left, (movL_x, movL_y - 2400))
        screen.blit(self.margin_left, (movL_x, movL_y - 3000))
        screen.blit(self.margin_left, (movL_x, movL_y - 3600))
        screen.blit(self.margin_left, (movL_x, movL_y - 4200))
        screen.blit(self.margin_left, (movL_x, movL_y - 4800))

        # movimento margem direita
        screen.blit(self.margin_right, (movR_x, movR_y))
        screen.blit(self.margin_right, (movR_x, movR_y + 600))
        screen.blit(self.margin_right, (movR_x, movR_y + 1200))
        screen.blit(self.margin_right, (movR_x, movR_y + 1800))
        screen.blit(self.margin_right, (movR_x, movR_y + 2400))
        screen.blit(self.margin_right, (movR_x, movR_y + 3000))
        screen.blit(self.margin_right, (movR_x, movR_y - 600))
        screen.blit(self.margin_right, (movR_x, movR_y - 1200))
        screen.blit(self.margin_right, (movR_x, movR_y - 1800))
        screen.blit(self.margin_right, (movR_x, movR_y - 2400))
        screen.blit(self.margin_right, (movR_x, movR_y - 3000))
        screen.blit(self.margin_right, (movR_x, movR_y - 3600))
        screen.blit(self.margin_right, (movR_x, movR_y - 4200))
        screen.blit(self.margin_right, (movR_x, movR_y - 4800))
    # move()