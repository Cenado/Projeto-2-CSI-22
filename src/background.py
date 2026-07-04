import pygame
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN_WIDTH

class Background:
    BACKGROUND_VELOCITY = 3.75
    MARGIN_LEFT_X = 740

    def __init__(self):
        background_fig = pygame.image.load("src/Sprites/Images/background.png")
        background_fig.convert()
        background_fig = pygame.transform.scale(background_fig, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self._background = background_fig

        margin_fig = pygame.image.load("src/Sprites/Images/margin.png")
        margin_fig.convert()
        margin_fig = pygame.transform.scale(margin_fig, (MARGIN_WIDTH, SCREEN_HEIGHT))
        self._margin_left = margin_fig
        self._margin_right = margin_fig

        self._bgY1 = 0
        self._bgX1 = 0

        self._bgY2 = SCREEN_HEIGHT
        self._bgX2 = 0

    def _update(self):
        self._bgY1 += self.BACKGROUND_VELOCITY
        self._bgY2 += self.BACKGROUND_VELOCITY
        if self._bgY1 >= SCREEN_HEIGHT:
            self._bgY1 = -SCREEN_HEIGHT
        if self._bgY2 >= SCREEN_HEIGHT:
            self._bgY2 = -SCREEN_HEIGHT

    def move(self, screen):
        self._update()

        screen.blit(self._background, (self._bgX1, self._bgY1))
        screen.blit(self._background, (self._bgX2, self._bgY2))

        screen.blit(self._margin_left, (self._bgX1, self._bgY1))
        screen.blit(self._margin_left, (self._bgX2, self._bgY2))

        screen.blit(self._margin_right, (self.MARGIN_LEFT_X, self._bgY1))
        screen.blit(self._margin_right, (self.MARGIN_LEFT_X, self._bgY2))