import pygame

class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
    def __init__(self):

        background_fig = pygame.image.load("Images/background.png")
        background_fig.convert()
        background_fig = pygame.transform.scale(background_fig, (800, 600))
        self.background = background_fig
        self.height = self.background.get_height()

        margin_left_fig = pygame.image.load("Images/margin_1.png")
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 600))
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 600))
        self.margin_right = margin_right_fig

        self.background_speed = 4
        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.height
        self.bgX2 = 0

        self.margin_left_x = 740
    # __init__()

    def _update(self):
        self.bgY1 += self.background_speed
        self.bgY2 += self.background_speed
        if self.bgY1 >= self.height:
            self.bgY1 = -self.height
        if self.bgY2 >= self.height:
            self.bgY2 = -self.height
    # update()

    def move(self, screen):
        self._update()

        screen.blit(self.background, (self.bgX1, self.bgY1))
        screen.blit(self.background, (self.bgX2, self.bgY2))

        screen.blit(self.margin_left, (self.bgX1, self.bgY1))
        screen.blit(self.margin_left, (self.bgX2, self.bgY2))

        screen.blit(self.margin_right, (self.margin_left_x, self.bgY1))
        screen.blit(self.margin_right, (self.margin_left_x, self.bgY2))
    # move()