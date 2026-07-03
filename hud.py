import pygame

class HUD:
    OPAQUE = 0
    LOST_COLOR = (255, 0, 0)
    SCORE_COLOR = (253, 231, 32)
    COLLIDED_COLOR = (255, 255, 255)

    score_text = "Score: "
    lost_text = "GAME OVER!"
    collided_text = "COLLIDED!"

    screen_width = 800
    screen_height = 600

    score_position = (0, 100)

    def __init__(self):
        self.score = 0

        self.font_warning = pygame.font.Font("Fonts/Fonte4.ttf", 100)
        self.render_lost_text = self.font_warning.render(self.lost_text, self.OPAQUE, self.LOST_COLOR)
        self.render_collided_text = self.font_warning.render(self.collided_text, self.OPAQUE, self.COLLIDED_COLOR)

        self.font_score = pygame.font.SysFont(None, 35)
        self.render_score_text = self.font_score.render(self.score_text + str(self.score), self.OPAQUE, self.SCORE_COLOR)
        #passou = font.render("Passou: " + str(h_passou), True, (255, 255, 128))

    def increment_score(self):
        self.score += 10
        self.render_score_text = self.font_score.render(self.score_text + str(self.score), self.OPAQUE, self.SCORE_COLOR)

    def reset_score(self):
        self.score = 0
        self.render_score_text = self.font_score.render(self.score_text + str(self.score), self.OPAQUE, self.SCORE_COLOR)

    def print_collided_text(self, screen):
        size = self.font_warning.size(self.collided_text)
        position = ((self.screen_width - size[0])/2, (self.screen_height - size[1])/2)

        screen.blit(self.render_collided_text, position)

    def print_lost_text(self, screen):
        size = self.font_warning.size(self.lost_text)
        position = ((self.screen_width - size[0])/2, (self.screen_height - size[1])/2)

        screen.blit(self.render_lost_text, position)

    def print_score(self, screen):
        screen.blit(self.render_score_text, self.score_position)
        #screen.blit(passou, (0, 50))
    