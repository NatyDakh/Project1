import pygame
import time
import constant
pygame.font.init()


class Life(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../grafic/life.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        """Инициализирует кота"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../grafic/cat.png')
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
        self.speed = 5
        self.jump_speed = 12
        self.onGround = False
        self.rect.x = 0
        self.rect.y = 0
        self.life = 3
        self.bite = 1
        self.attack = False
        self.total_score = 0
        self.bonus = 1
        self.shield = False
        self.time_start = 0
        self.have_bonus = False

    def grav(self):
        """Гравитация для объекта"""
        if self.onGround:
            return
        if self.move_y == 0:
            self.move_y = 1
        else:
            self.move_y += 0.35
        # остановка_при_соприкосновении_с_землей
        if self.rect.y >= constant.SCREEN_HEIGHT - self.rect.height and self.move_y >= 0:
            if not self.shield:
                self.move_y = 0
                self.rect.y = 0
                self.life -= 1

    def collide(self, x, y, platforms):
        """Функция для взаимодействия с платформами"""
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if x > 0:  # если движется вправо
                    self.rect.right = p.rect.right  # то не движется вправо
                if x < 0:  # если движется влево
                    self.rect.left = p.rect.left  # то не движется влево
                if y > 0:
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.move_y = 0  # и энергия падения пропадает
                if y < 0:
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.move_y = 0

    def update(self, platforms):
        """Обновление котика на экране"""
        if not self.onGround:
            self.grav()
        self.onGround = False
        if self.move_x < 0 and self.rect.left >= 0:
            self.rect.centerx += self.move_x
        elif self.move_x > 0:
            self.rect.centerx += self.move_x
        self.collide(self.move_y, 0, platforms)
        self.rect.y += self.move_y
        self.collide(0, self.move_y, platforms)

    def jump(self):
        """Обработка прыжка"""
        self.move_y = -self.jump_speed

    def go_right(self):
        """Движение в право"""
        self.move_x = self.speed

    def go_left(self):
        """Движение в лево"""
        self.move_x = (-1) * self.speed

    def stop(self):
        """Остановка кота"""
        self.move_y = 0
        self.move_x = 0
        self.attack = False

    def change_attack(self):
        """Возведение флага атаки"""
        self.attack = True

    def draw_life(self, screen):
        """Отрисовка жизней"""
        for i in range(self.life):
            life = Life(i * 40 + 10 + i * 5)
            screen.blit(life.image, life.rect)
        self.draw_score(screen, 15, 65, 60)
        if self.life == 0:
            self.speed = 0
            self.jump_speed = 0
            """Отрисовка последнего экрана"""
            s = pygame.Surface((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            s.set_alpha(150)
            s.fill((63, 71, 89))
            screen.blit(s, (0, 0))
            self.draw_score(screen, 50, constant.SCREEN_WIDTH / 2,
                            constant.SCREEN_HEIGHT / 2)

    def draw_score(self, screen, size, x, y):
        """Рисование счета на экране"""
        font1 = pygame.font.Font('../grafic/segoesc.ttf', size)
        text1 = font1.render('Total score: ' + str(self.total_score), True, (0, 0, 0))
        textRect1 = text1.get_rect()
        textRect1.x = x - textRect1.width/2
        textRect1.y = y - textRect1.height/2
        screen.blit(text1, textRect1)

    def no_bonus(self):
        """Обнуление бонусов через 10 секунд"""
        if time.time() - self.time_start > 10 and self.have_bonus:
            self.speed = 5
            self.bonus = 1
            self.shield = False
            self.time_start = 0
