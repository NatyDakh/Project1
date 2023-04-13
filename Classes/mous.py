import pygame


class Mouse(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../grafic/mouse.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.life = 1
        self.attack = True
        self.bit = 1

    def die(self, cat, active):
        """Процесс сметри мышенка"""
        cat.total_score += 3
        active.remove(self)
