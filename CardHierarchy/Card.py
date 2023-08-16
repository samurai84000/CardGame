import pygame
from pygame.sprite import Group


class Card(pygame.sprite.Sprite):
    def __init__(self, name, image_path, cost, x, y):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sprites = Group()

    def add_sprite(self, sprite):
        self.sprites.add(sprite)

    def remove_sprite(self, sprite):
        self.sprites.remove(sprite)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.sprites.draw(screen)
