import pygame
import time
"""Описание класса бонусов, 1=двойные монетки, 2=щит, 3=ускорение"""


class Mint(pygame.sprite.Sprite):
    def __init__(self, x, y, num=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../grafic/mint.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bonus = num

    def change_cat(self, cat):
        """Функция меняющая кота, в зависимоти от бонуса"""
        if self.bonus == 1 and cat.bonus < 2:
            cat.bonus *= 2
        if self.bonus == 2:
            cat.shield = True
        if self.bonus == 3:
            cat.speed += 3
        cat.time_start = time.time()
        cat.have_bonus = True
