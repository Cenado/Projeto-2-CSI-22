import pygame
from abc import ABC

class Entity(ABC):
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Player(Entity):
    def __init__(self, x, y):
        image = pygame.image.load("Images/player.png")
        image.convert()
        image = pygame.transform.scale(image, (90, 90))

        super().__init__(image, x, y)

    def move(self, dx):
        self.x += dx

    def collided_with_border(self, left_border, right_border):
        return self.x < left_border or self.x > right_border

class Hazard(Entity):
    def __init__(self, image_path, x, y):
        image = self.load_image(image_path)
        super().__init__(image, x, y)

    def load_image(self, image_path):
        image = pygame.image.load(image_path)
        image.convert()
        return pygame.transform.scale(image, (130, 130))

    def respawn(self, image_path, x, y):
        self.image = self.load_image(image_path)
        self.x = x
        self.y = y

    def move(self, dy):
        self.y += dy