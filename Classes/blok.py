import pygame


class Bloc(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, num=1):
        """Инициализирует блок"""
        pygame.sprite.Sprite.__init__(self)
        if num == 1:
            self.image = pygame.image.load('C:/Users/natyd/PycharmProjects/Project1/grafic/bloktype1.png')
        else:
            self.image = pygame.image.load('C:/Users/natyd/PycharmProjects/Project1/grafic/bloktype2.png')
        self.rect = self.image.get_rect()
        self.num = num  # тип платформы
        self.rect.x = xloc
        self.rect.y = yloc

    def coord(self):
        return self.rect.left, self.rect.top
