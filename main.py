import pygame as pyg
import control
from Classes.cat import Cat
import constant
import generator


def run():
    clock = pyg.time.Clock()
    pyg.init()
    screen = pyg.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
    pyg.display.set_caption("Мурьяна")
    cat = Cat()
    active_sprite_list = pyg.sprite.Group()
    platforms = pyg.sprite.Group()
    active_sprite_list.add(cat)
    move = 0
    generator.generator(platforms, cat, active_sprite_list)

    while True:
        control.events(cat, screen)
        screen.fill(constant.bg_color)
        control.interaction(active_sprite_list, cat)
        cat.no_bonus()
        active_sprite_list.update(platforms)
        active_sprite_list.draw(screen)
        cat.draw_life(screen)
        # Процесс передвижения экрана
        if move == 300:
            generator.generator(platforms, cat, active_sprite_list)
            move = 0
        if constant.SCREEN_WIDTH - cat.rect.right < 300:
            move += control.move(active_sprite_list, platforms)
        else:
            clock.tick(constant.FPS)
        pyg.display.flip()


run()
