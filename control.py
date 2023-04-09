import pygame as pyg, sys
from mous import Mouse
from mint import Mint
from milk import Milk
from blok import Bloc


def events(cat, screen):
    """оброботка событий"""
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        if event.type == pyg.KEYDOWN:  # add a, w and d
            if event.key == pyg.K_LEFT or event.key == pyg.K_a:
                cat.go_left()
            if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                cat.go_right()
            if event.key == pyg.K_UP or event.key == pyg.K_w:
                cat.jump()
            if event.key == pyg.K_SPACE:
                cat.change_attack()
        if event.type == pyg.KEYUP:
            if (event.key == pyg.K_LEFT or event.key == pyg.K_a) and cat.move_x < 0:
                cat.stop()
            if (event.key == pyg.K_RIGHT or event.key == pyg.K_d) and cat.move_x > 0:
                cat.stop()
            if event.key == pyg.K_SPACE:
                cat.stop()


def interaction(active, cat):
    """Взаймодействие между объектами"""
    enemise = pyg.sprite.spritecollide(cat, active, False)
    for i in enemise:
        if type(i) == Bloc:
            continue
        if type(i) == Milk:
            active.remove(i)
            cat.total_score += i.score * cat.bonus
        if type(i) == Mint:
            active.remove(i)
            i.change_cat(cat)
        if type(i) == Mouse:
            if not cat.attack:
                cat.life -= 1
            else:
                i.life -= cat.bite
            if i.life == 0:
                i.die(cat, active)


def move(active, platforms):
    """Двигает экрае при достижения края"""
    for i in active:
        i.rect.x -= 10
        if i.rect.x < 0:
            active.remove(i)
            if type(i) == Bloc:
                platforms.remove(i)
    return 10
