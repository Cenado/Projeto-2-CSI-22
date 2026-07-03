import pygame
import random
from abc import ABC

class Entity(ABC):
    def __init__(self, image, x, y):
        self.image = image
        self.hitbox = image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)

class Player(Entity):
    WIDTH = 90
    HEIGHT = 90

    def __init__(self, x, y):
        image = pygame.image.load("Images/player.png")
        image.convert()
        image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

        super().__init__(image, x, y)

    def move(self, dx):
        self.hitbox.x += dx

    def collided_with_border(self, left_border, right_border):
        return self.hitbox.left < left_border or self.hitbox.right > right_border

class Hazard(Entity):
    WIDTH = 130
    HEIGHT = 130

    def __init__(self, x, y):
        self.images = [
            "Images/nave.png",
            "Images/satelite.png",
            "Images/cometa.png",
            "Images/planeta.png",
            "Images/ameaca.png"]

        image = self.load_image(self.images[0])
        super().__init__(image, x, y)

    def load_image(self, image_path):
        image = pygame.image.load(image_path)
        image.convert()
        return pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

    def respawn(self, left_limit, right_limit):
        self.image = self.load_image(random.choice(self.images))
        self.hitbox.x = random.randrange(left_limit, right_limit)
        self.hitbox.y = -self.hitbox.height

    def move(self, dy):
        self.hitbox.y += dy

    def exited_screen(self, screen_height):
        return self.hitbox.y > screen_height
    
    def collided(self, player):
        return self.hitbox.colliderect(player.hitbox)