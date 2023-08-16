import pygame
import pygame.sprite


class Level:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.Cards = {}

    def __run__(self):
        self.__drawBoard__()

    def __drawBoard__(self):
        for sprite in self.all_sprites:
            self.surface.blit(sprite.image)


