#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame

from player import *
from menu import *
from intarface import *
from settings_menuu import *
import generator
import npc

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
    """
    :param camera:
    :param target_rect:
    :return:
    """
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2
    return Rect(l, t, w, h)


def draw_map(chank, entities, platforms):
    """
    1) принимает массив из чесел, которые означают номер блока
    2) принимает группу спрайтов, в которую записывает значения получннные из массива 1
    3) принимает массив класса блок, в которую записывает их координаты, размеры и вид блока
    :param chank:
    :param entities:
    :param platforms:
    :return:
    """
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
            elif col == 8:
                pf = Platform(x, y, col)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 960 * chank.chank_num  # на каждой новой строчке начинаем с нуля




def main(save=False):
    """
    главный цикл, который проверяе все условия.
    !) инциализирует pygame
    2) инициализирует все переменные(окно игры, задний фон, клавиши, звуки, карту, нпс, сохранения, время суток и рисует все на окне
    :param save:
    :return:
    """
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY, FULLSCREEN)  # Создаем окошко
    pygame.display.set_caption("Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    bgbl = image.load('textures//background//background.jpg').convert(24)
    skale = transform.scale(bgbl, (WIN_WIDTH, WIN_HEIGHT))
    time_day = 0
    day = False
    old_time_day = 0
    setttings_menu = False
    deystvie = False
    block_num = 1
    npc_one = npc.Npc(100, 0)
    # добавим звуков и музыки
    # mixer.pre_init(44100, -16, 1, 512)
    # mixer.init()
    # shag = mixer.Sound('sounds/music/fon.ogg')
    # panche = mixer.Sound('sounds/environment/shag.ogg')
    # shag.set_volume(0.3)
    # shag.play(-1)
    # old_time = 0
    # click_sound = mixer.Sound('sounds//environment//mm_button.ogg')
    chank_one = generator.Mymap(1)
    # chank_one.line_y(29, 1)
    # chank_two = generator.Mymap(-1)
    # chank_two.line_y(29, 2)
    # chank_tre = generator.Mymap(-2)
    # chank_tre.line_y(29, 1)
    a = chank_one.chank_mass(20)
    for i in range(3):
        n = a[i]
        for e in range(1):
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
    entities.add(npc_one)
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
                tmp_save = 0
                save_new.save('rect', hero.rect)
                for elem in platforms:
                    tmp_save += 1
                    save_new.save(str(tmp_save), elem)

            if e.type == KEYDOWN and e.key == K_F8:
                hero.rect = save_new.load('rect')

            # if e.type == KEYDOWN and e.key == K_e:
            #    new_time = time.get_ticks()
            #    if new_time - old_time > 1000:
            #        old_time = new_time
            #        panche.play()
            if e.type == KEYDOWN and e.key == K_TAB:
                pass
                interface(screen, WIN_WIDTH, WIN_HEIGHT)
            if e.type == KEYDOWN and e.key == K_F3:
                if setttings_menu:
                    setttings_menu = False
                else:
                    setttings_menu = True

            if e.type == KEYDOWN and e.key == K_1:   # меняем блоки
                block_num += 1
                if block_num > 7:
                    block_num = 1

            if e.type == MOUSEBUTTONDOWN and e.button == 4:  # меняем блоки вперед
                block_num += 1
                if block_num > 7:
                    block_num = 1
            if e.type == MOUSEBUTTONDOWN and e.button == 5:   # меняем блоки назад
                block_num -= 1
                if block_num < 1:
                    block_num = 7

        #
        #if time_day <= 0 or day:  # добавим день и ночь
         #   time_day += 0.5
          #  day = True
           # if time_day >= 255:
            #    old_time_day += 1
             #   if old_time_day >= 1000:
              #      day = False
               #     old_time_day = 0
        #else:
            #time_day -= 0.5
        screen.fill((0, 0, 0))
        #skale.set_alpha(time_day)
        screen.blit(skale, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero)  # центризируем камеру относительно персонажа
        # передвижение

        # entities.draw(screen) # отображение
        for e in entities:                                               # draw settings menu
            screen.blit(e.image, camera.apply(e))
        if setttings_menu:
            settings_menu(hero, screen, block_num)

        remove_bolck(platforms, camera, entities, hero)                    # удаляем блоки
        add_block(platforms, camera, entities, hero, block_num, npc_one)   # добавляем блоки
        hero.update(left, right, up, platforms)                            # hbcetv uthjz
        npc_one.update(False, False, False, platforms, hero, screen, camera, WIN_WIDTH, WIN_HEIGHT)  # draw npc
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    menu()
