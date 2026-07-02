import pygame
from abc import ABC

class Entity(ABC):
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y)) #TODO: substituir por self.x e self.y quando a lógica da movimentação for transferida de Game

class Player(Entity):
    def __init__(self, x, y):
        image = pygame.image.load("Images/player.png")
        image.convert()
        image = pygame.transform.scale(image, (90, 90))

        super().__init__(image, x, y)

class Hazard(Entity):
    def __init__(self, img, x, y):
        image = pygame.image.load(img)
        image.convert()
        image = pygame.transform.scale(image, (130, 130))

        super().__init__(image, x, y)