import pygame
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN_WIDTH
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, image, x, y):
        self.image = image
        self.hitbox = image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)

    @abstractmethod
    def reset(self):
        raise NotImplementedError

class Player(Entity):
    WIDTH = 90
    HEIGHT = 90
    DIST_TO_BOTTOM = 125
    SPEED = 2.25
    LEFT_BORDER = 45
    RIGHT_BORDER = 758

    def __init__(self):
        image = pygame.image.load("Images/player.png")
        image.convert()
        image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

        x = (SCREEN_WIDTH - self.WIDTH) / 2
        y = SCREEN_HEIGHT - self.DIST_TO_BOTTOM

        super().__init__(image, x, y)

    def reset(self):
        self.hitbox.x = (SCREEN_WIDTH - self.WIDTH) / 2
        self.hitbox.y = SCREEN_HEIGHT - self.DIST_TO_BOTTOM

    def move(self, direction):
        self.hitbox.x += direction * self.SPEED

    def collided_with_border(self):
        return self.hitbox.left < self.LEFT_BORDER or self.hitbox.right > self.RIGHT_BORDER

class Hazard(Entity):
    WIDTH = 130
    HEIGHT = 130
    Y_SPAWN = -500
    SPEED = 6.56

    def __init__(self):
        self.images = [
            "Images/nave.png",
            "Images/satelite.png",
            "Images/cometa.png",
            "Images/planeta.png",
            "Images/ameaca.png"]

        image = self.load_image(self.images[0])
        x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        y = self.Y_SPAWN

        super().__init__(image, x, y)

    def reset(self):
        self.hitbox.x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        self.hitbox.y = self.Y_SPAWN

    def load_image(self, image_path):
        image = pygame.image.load(image_path)
        image.convert()
        return pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

    def respawn(self):
        self.image = self.load_image(random.choice(self.images))
        self.hitbox.x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        self.hitbox.y = -self.hitbox.height

    def move(self):
        self.hitbox.y += self.SPEED

    def exited_screen(self):
        return self.hitbox.y > SCREEN_HEIGHT
    
    def collided(self, player):
        return self.hitbox.colliderect(player.hitbox)