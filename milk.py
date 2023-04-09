import pygame
"""Описание класса монеток"""


class Milk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('grafic/milk.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score = 1
