#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame

from player import *
from blocks import *
from menu import *
from intarface import *
from settings_menuu import *
import generator

# Объявляем переменные
WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def main(save=False):
    global WIN_WIDTH, WIN_HEIGHT
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY, FULLSCREEN)  # Создаем окошко
    pygame.display.set_caption("Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    bgbl = image.load('textures//background//background.jpg')
    skale = transform.scale(bgbl, (WIN_WIDTH, WIN_HEIGHT))

    # добавим звуков и музыки
    # mixer.pre_init(44100, -16, 1, 512)
    # mixer.init()
    # shag = mixer.Sound('sounds/music/fon.ogg')
    # panche = mixer.Sound('sounds/environment/shag.ogg')
    # shag.set_volume(0.3)
    # shag.play(-1)
    # old_time = 0
    # click_sound = mixer.Sound('sounds//environment//mm_button.ogg')
    chank_one = generator.Mymap()
    chank_one.line_y(24, 1)
    chank_one.line_y(0, 1)
    chank_one.line_x(0, 1)
    chank_one.line_x(18, 1)
    chank_one.cube(5, 5, 5, 1)
    setttings_menu = False
    #

    hero = Player(32, 64)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    entities.add(hero)

    level = [
        "------------------------------------------",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "-                                        -",
        "------------------------------------------"]

    # Sve File
    if save:
        save = Save('Save')
        hero.rect = save.load('rect')
    # load save
    save_new = Save('Save_new')
    #

    #

    # /////
    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in chank_one.chank:  # вся строка
        for col in row:  # каждый символ
            if col == 1:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)

            elif col == "+":
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == "*":
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == "/":
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 'a':
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 't':
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 'd':
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)

    run = True
    while run:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True

            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False

            if e.type == KEYDOWN and e.key == K_ESCAPE:
                run = False

            if e.type == KEYDOWN and e.key == K_F5:
                save_new.save('rect', hero.rect)

            if e.type == KEYDOWN and e.key == K_F8:
                hero.rect = save_new.load('rect')

            # if e.type == KEYDOWN and e.key == K_e:
            #    new_time = time.get_ticks()
            #    if new_time - old_time > 1000:
            #        old_time = new_time
            #        panche.play()

            if e.type == KEYDOWN and e.key == K_TAB:
                interface(screen, bg)

            if e.type == KEYDOWN and e.key == K_F3:
                if setttings_menu:
                    setttings_menu = False
                else:
                    setttings_menu = True

        screen.blit(skale, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero)  # центризируем камеру относительно персонажа
        # передвижение

        # entities.draw(screen) # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        if setttings_menu:
            settings_menu(hero, screen)
        hero.update(left, right, up, platforms)
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    menu()
