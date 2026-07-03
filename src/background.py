import pygame
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN_WIDTH

class Background:
    BACKGROUND_VELOCITY = 3.75
    MARGIN_LEFT_X = 740

    def __init__(self):
        background_fig = pygame.image.load("src/Sprites/Images/background.png")
        background_fig.convert()
        background_fig = pygame.transform.scale(background_fig, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = background_fig

        margin_fig = pygame.image.load("src/Sprites/Images/margin.png")
        margin_fig.convert()
        margin = pygame.transform.scale(margin_fig, (MARGIN_WIDTH, SCREEN_HEIGHT))
        self.margin_left = margin
        self.margin_right = margin

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = SCREEN_HEIGHT
        self.bgX2 = 0

    def _update(self):
        self.bgY1 += self.BACKGROUND_VELOCITY
        self.bgY2 += self.BACKGROUND_VELOCITY
        if self.bgY1 >= SCREEN_HEIGHT:
            self.bgY1 = -SCREEN_HEIGHT
        if self.bgY2 >= SCREEN_HEIGHT:
            self.bgY2 = -SCREEN_HEIGHT

    def move(self, screen):
        self._update()

        screen.blit(self.background, (self.bgX1, self.bgY1))
        screen.blit(self.background, (self.bgX2, self.bgY2))

        screen.blit(self.margin_left, (self.bgX1, self.bgY1))
        screen.blit(self.margin_left, (self.bgX2, self.bgY2))

        screen.blit(self.margin_right, (self.MARGIN_LEFT_X, self.bgY1))
        screen.blit(self.margin_right, (self.MARGIN_LEFT_X, self.bgY2))