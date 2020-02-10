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
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 600  # Высота
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
    mose = pygame.mouse.get_pos()
    l += -mose[0] / 15
    t += -mose[1] / 15
    return Rect(l, t, w, h)


def draw_map(chank, entities, platforms):
    y = 0
    x = 960 * chank.chank_num  # координаты
    for row in chank.chank:  # вся строка
        for col in row:  # каждый символ
            if col == 1:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)

            elif col == 2:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 3:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 4:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 5:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 6:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 6:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            elif col == 7:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 960 * chank.chank_num  # на каждой новой строчке начинаем с нуля


def remove_bolck(platforms, camera, entities):
    mouse_pl = mouse.get_pos()
    mouse_pl_click = mouse.get_pressed()
    tmp = -1
    for e in platforms:
        tmp += 1
        if e.rect.x < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w:
            if e.rect.y < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h:
                if mouse_pl_click[0] == 1:
                    platforms.pop(tmp)
                    entities.remove(e)


def add_block(platforms, camera, entities):
    mouse_pl = mouse.get_pos()
    mouse_pl_click = mouse.get_pressed()
    tmp = -1
    for e in platforms:
        tmp += 1
        if e.rect.x < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w:
            if e.rect.y + e.rect.h < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h * 2:
                if mouse_pl_click[2] == 1:
                    pl = Platform(e.rect.x, e.rect.y + e.rect.h, 1)
                    platforms.append(pl)
                    entities.add(pl)


def main(save=False):
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    bgbl = image.load('textures//background//background.jpg').convert(24)
    skale = transform.scale(bgbl, (WIN_WIDTH, WIN_HEIGHT))
    time_day = 0
    day = False
    old_time_day = 0
    deystvie = False

    # добавим звуков и музыки
    # mixer.pre_init(44100, -16, 1, 512)
    # mixer.init()
    # shag = mixer.Sound('sounds/music/fon.ogg')
    # panche = mixer.Sound('sounds/environment/shag.ogg')
    # shag.set_volume(0.3)
    # shag.play(-1)
    # old_time = 0
    # click_sound = mixer.Sound('sounds//environment//mm_button.ogg')
    chank_one = generator.Mymap(0)
    # chank_one.line_y(29, 1)
    # chank_two = generator.Mymap(-1)
    # chank_two.line_y(29, 2)
    # chank_tre = generator.Mymap(-2)
    # chank_tre.line_y(29, 1)
    setttings_menu = False
    a = generator.chank_mass(20)
    for i in range(3):
        n = a[i]
        for e in range(23):
            n.line_y(29 - e, 3 + i)

    #

    hero = Player(0, 0)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False
    #

    #
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
    for elem in a:
        draw_map(elem, entities, platforms)
    # draw_map(chank_one, entities, platforms)
    # draw_map(chank_two, entities, platforms)
    # draw_map(chank_tre, entities, platforms)
    #

    # /////
    timer = pygame.time.Clock()

    #

    #
    total_level_width = len(chank_one.chank[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(chank_one.chank) * PLATFORM_HEIGHT  # высоту

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
                #
            if e.type == KEYDOWN and e.key == K_e:
                deystvie = True
            if e.type == KEYUP and e.key == K_e:
                deystvie = False
                #
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
        #
        if time_day <= 0 or day:  # добавим день и ночь
            time_day += 0.5
            day = True
            if time_day >= 255:
                old_time_day += 1
                if old_time_day >= 1000:
                    day = False
                    old_time_day = 0
        else:
            time_day -= 0.5
        screen.fill((0, 0, 0))
        skale.set_alpha(time_day)
        screen.blit(skale, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero)  # центризируем камеру относительно персонажа
        # передвижение

        # entities.draw(screen) # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        if setttings_menu:
            settings_menu(hero, screen, total_level_width, total_level_height, camera, platforms)

        remove_bolck(platforms, camera, entities)
        add_block(platforms, camera, entities)
        hero.update(left, right, up, platforms)

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    menu()
