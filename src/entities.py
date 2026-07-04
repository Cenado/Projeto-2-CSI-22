import pygame
import random
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN_WIDTH
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, image, x, y):
        self._image = image
        self._hitbox = image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self._image, self._hitbox)

    @abstractmethod
    def reset(self):
        raise NotImplementedError
    
    @abstractmethod
    def move(self):
        raise NotImplementedError

class Player(Entity):
    WIDTH = 90
    HEIGHT = 90
    DIST_TO_BOTTOM = 125
    SPEED = 2.25
    LEFT_BORDER = 45
    RIGHT_BORDER = 758

    def __init__(self):
        image = pygame.image.load("src/Sprites/Images/player.png")
        image.convert()
        image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

        x = (SCREEN_WIDTH - self.WIDTH) / 2
        y = SCREEN_HEIGHT - self.DIST_TO_BOTTOM

        super().__init__(image, x, y)

    def reset(self):
        self._hitbox.x = (SCREEN_WIDTH - self.WIDTH) / 2
        self._hitbox.y = SCREEN_HEIGHT - self.DIST_TO_BOTTOM

    def move(self, direction):
        self._hitbox.x += direction * self.SPEED

    def collided_with_border(self):
        return self._hitbox.left < self.LEFT_BORDER or self._hitbox.right > self.RIGHT_BORDER

class Hazard(Entity):
    WIDTH = 130
    HEIGHT = 130
    Y_SPAWN = -500
    SPEED = 6.56

    def __init__(self):
        self._images = [
            "src/Sprites/Images/nave.png",
            "src/Sprites/Images/satelite.png",
            "src/Sprites/Images/cometa.png",
            "src/Sprites/Images/planeta.png",
            "src/Sprites/Images/ameaca.png"]

        image = self._load_image(self._images[0])
        x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        y = self.Y_SPAWN

        super().__init__(image, x, y)

    def reset(self):
        self._hitbox.x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        self._hitbox.y = self.Y_SPAWN

    def _load_image(self, image_path):
        image = pygame.image.load(image_path)
        image.convert()
        return pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

    def respawn(self):
        self._image = self._load_image(random.choice(self._images))
        self._hitbox.x = random.randrange(MARGIN_WIDTH, SCREEN_WIDTH - MARGIN_WIDTH - self.WIDTH)
        self._hitbox.y = -self._hitbox.height

    def move(self):
        self._hitbox.y += self.SPEED

    def exited_screen(self):
        return self._hitbox.y > SCREEN_HEIGHT
    
    def collided(self, player):
        return self._hitbox.colliderect(player._hitbox)