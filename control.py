import pygame as pyg
import sys
from Classes.mous import Mouse
from Classes.mint import Mint
from Classes.milk import Milk
from Classes.blok import Bloc


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
            if (event.key == pyg.K_UP or event.key == pyg.K_w):
                cat.jump()
            if event.key == pyg.K_SPACE:
                cat.change_attack()
        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT or event.key == pyg.K_a:
                cat.stop()
            if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                cat.stop()
            if event.key == pyg.K_SPACE:
                cat.stop()
                cat.onGround = True


def interaction(active, cat, platforms):
    """Взаймодействие между объектами"""
    enemise = pyg.sprite.spritecollide(cat, active, False)
    for i in enemise:
        if type(i) == Bloc:
            cat.update(platforms)
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
