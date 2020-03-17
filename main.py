#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame

from player import *
from menu import *
from intarface import *
from settings_menuu import *
from camera import *
import generator
import npc

# Объявляем переменные
WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"


def main(save=False):
    """
    главный цикл, который проверяе все условия.
    !) инциализирует pygame
    2) инициализирует все переменные(окно игры, задний фон, клавиши, звуки, карту, нпс, сохранения, время суток и рисует все на окне
    :param save:
    :return:
    """
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    bgbl = image.load('textures//background//background.jpg').convert(24)
    skale = transform.scale(bgbl, (WIN_WIDTH, WIN_HEIGHT))  # background image
    setttings_menu = False

    block_num = 1
    npc_one = npc.Npc(100, 0)  # 1 npc
    chank_one = generator.Mymap(1)  # 1 chanck
    massiv_map = chank_one.chank_mass(20)
    for i in range(3):  # заполняем карту блоками
        n = massiv_map[i]
        for e in range(1):
            n.line_y(29 - e, 3 + i)

    hero = Player(0, 0)  # создаем героя по (x,y) координатам

    left = right = False  # по умолчанию - стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    entities.add(npc_one)
    # Save File
    if save:
        save = Save('Save')
        hero.rect = save.load('rect')

    save_new = Save('Save_new')
    for elem in massiv_map:
        draw_map(elem, entities, platforms)

    timer = pygame.time.Clock()  # fps game

    total_level_width = len(chank_one.chank[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(chank_one.chank) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)  # camera init
    run = True
    while run:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN and e.key == K_SPACE:  # прыгаем
                up = True
            if e.type == KEYDOWN and e.key == K_a:  # run left
                left = True
            if e.type == KEYDOWN and e.key == K_d:  # run right
                right = True
            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:  # qut in game
                run = False
            if e.type == KEYDOWN and e.key == K_F5:  # save game
                tmp_save = 0
                save_new.save('rect', hero.rect)
                for elem in platforms:
                    tmp_save += 1
                    save_new.save(str(tmp_save), elem)
            if e.type == KEYDOWN and e.key == K_F8:  # load game
                hero.rect = save_new.load('rect')

            if e.type == KEYDOWN and e.key == K_TAB:  # run interface
                interface(screen, WIN_WIDTH, WIN_HEIGHT)

            if e.type == KEYDOWN and e.key == K_F3:  # active or passive settings menu
                if setttings_menu:
                    setttings_menu = False
                else:
                    setttings_menu = True

            if e.type == KEYDOWN and e.key == K_1:  # меняем блоки
                block_num += 1
                if block_num > 7:
                    block_num = 1

            if e.type == MOUSEBUTTONDOWN and e.button == 4:  # меняем блоки вперед
                block_num += 1
                if block_num > 7:
                    block_num = 1
            if e.type == MOUSEBUTTONDOWN and e.button == 5:  # меняем блоки назад
                block_num -= 1
                if block_num < 1:
                    block_num = 7

        screen.fill((0, 0, 0))  # black background
        screen.blit(skale, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero)  # центризируем камеру относительно персонажа


        # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        if setttings_menu:
            settings_menu(hero, screen, block_num, npc_one)

        remove_bolck(platforms, camera, entities, hero)  # удаляем блоки
        add_block(platforms, camera, entities, hero, block_num, npc_one)  # добавляем блоки
        hero.update(left, right, up, platforms)
        npc_one.update(False, True, False, platforms, hero, screen, camera, WIN_WIDTH, WIN_HEIGHT)  # draw npc
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    menu()
