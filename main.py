import pygame as pyg, control
from cat import Cat
from blok import Bloc
import constant, generator


def run():
    clock = pyg.time.Clock()
    pyg.init()
    screen = pyg.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
    pyg.display.set_caption("Мурьяна")
    cat = Cat()
    active_sprite_list = pyg.sprite.Group()
    platforms = pyg.sprite.Group()
    active_sprite_list.add(cat)
    generator.generator(platforms, cat, active_sprite_list)

    while True:
        control.events(cat, screen)
        screen.fill(constant.bg_color)
        control.interaction(active_sprite_list, cat)
        cat.no_bonus()
        active_sprite_list.update(platforms)
        active_sprite_list.draw(screen)
        cat.draw_life(screen)
        if cat.rect.right == constant.SCREEN_WIDTH:
            generator.generator(platforms, cat, active_sprite_list)
            control.move(active_sprite_list, platforms)
        if cat.life == 0:
            clock.tick(10)
            cat.speed = 0
            cat.jump_speed = 0
            """Отрисовка последнего экрана"""
            s = pyg.Surface((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            s.set_alpha(150)
            s.fill((63, 71, 89))
            screen.blit(s, (0, 0))
            cat.draw_score(screen, 50, constant.SCREEN_WIDTH / 2, constant.SCREEN_HEIGHT / 2)
        else:
            clock.tick(constant.FPS)
        pyg.display.flip()

run()
