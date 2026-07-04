import pygame
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class HUD:
    OPAQUE = 0
    TRANSPARENT = 1
    LOST_COLOR = (255, 0, 0)
    SCORE_COLOR = (253, 231, 32)
    COLLIDED_COLOR = (255, 255, 255)

    SCORE_TEXT = "Score: "
    LOST_TEXT = "GAME OVER!"
    COLLIDED_TEXT = "COLLIDED!"

    SCORE_FONT_SIZE = 35
    WARNING_FONT_SIZE = 100

    SCORE_POSITION = (0, 100)
    SCORE_INCREMENT = 10

    def __init__(self):
        self._score = 0

        self._font_warning = pygame.font.Font("src/Sprites/Fonts/Fonte4.ttf", self.WARNING_FONT_SIZE)
        self._render_lost_text = self._font_warning.render(self.LOST_TEXT, self.OPAQUE, self.LOST_COLOR)
        self._render_collided_text = self._font_warning.render(self.COLLIDED_TEXT, self.OPAQUE, self.COLLIDED_COLOR)

        self._font_score = pygame.font.SysFont(None, self.SCORE_FONT_SIZE)
        self._render_score_text = self._font_score.render(self.SCORE_TEXT + str(self._score), self.OPAQUE, self.SCORE_COLOR)

    def increment_score(self):
        self._score += self.SCORE_INCREMENT
        self._render_score_text = self._font_score.render(self.SCORE_TEXT + str(self._score), self.OPAQUE, self.SCORE_COLOR)

    def reset_score(self):
        self._score = 0
        self._render_score_text = self._font_score.render(self.SCORE_TEXT + str(self._score), self.OPAQUE, self.SCORE_COLOR)

    def print_collided_text(self, screen):
        size = self._font_warning.size(self.COLLIDED_TEXT)
        position = ((SCREEN_WIDTH - size[0])/2, (SCREEN_HEIGHT - size[1])/2)

        screen.blit(self._render_collided_text, position)

    def print_lost_text(self, screen):
        size = self._font_warning.size(self.LOST_TEXT)
        position = ((SCREEN_WIDTH - size[0])/2, (SCREEN_HEIGHT - size[1])/2)

        screen.blit(self._render_lost_text, position)

    def print_score(self, screen):
        screen.blit(self._render_score_text, self.SCORE_POSITION)