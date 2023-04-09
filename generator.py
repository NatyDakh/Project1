import random
import blok, mint, milk, mous
import constant, levels


def dop(active, x_plat, y_plat):
    """Генерация объектов на платформах"""
    t = random.randint(0, 11)
    if t == 4 or t == 5 or t == 9:
        count = random.randint(1, 3)
        for i in range(count):
            k = milk.Milk(x_plat + 35 * int(i != 0), y_plat - 40)
            active.add(k)
    if t == 6:
        k = mint.Mint(x_plat + 15, y_plat - 30)
        active.add(k)
    if t == 11 and x_plat != 0:
        k = mous.Mouse(x_plat + 30, y_plat - 60)
        active.add(k)


def generator(platforms, cat, active):
    """Генерерует чертвети экрана, на каждой находится какие-то предметы"""
    if not platforms:
        for i in range(4):
            number = random.randint(1, 3)
            level = levels.levels[number][random.randint(0, 1)]
            for n, j in enumerate(level, start=0):
                for pos in range(3):
                    if j[pos] == '_':
                        b = blok.Bloc(i * 300 + pos * 100, 150 * (n/2 + 1))
                        platforms.add(b)
                        active.add(b)
                        dop(active, i * 300 + pos * 100, 150 * (n/2 + 1))
                    if j[pos] == '|':
                        b = blok.Bloc(i * 300 + pos * 100 - 15, 150 * ((n - 1)/2 + 1) + 50, num=2)
                        platforms.add(b)
                        active.add(b)
        active.remove(cat)
        active.add(cat)
    else:
        number = random.randint(1, 3)
        level = levels.levels[number][random.randint(0, 1)]
        for n, j in enumerate(level, start=0):
            for pos in range(3):
                if j[pos] == '_':
                    b = blok.Bloc(1200 + pos * 100, 150 * (n / 2 + 1))
                    platforms.add(b)
                    active.add(b)
                    dop(active, 1200 + pos * 100, 150 * (n / 2 + 1))
                if j[pos] == '|':
                    b = blok.Bloc(1200 + pos * 100 - 15, 150 * ((n - 1) / 2 + 1) + 50, num=2)
                    platforms.add(b)
                    active.add(b)
    active.remove(cat)
    active.add(cat)


