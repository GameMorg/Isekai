#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Platform(sprite.Sprite):
    """
    блоки
    """

    def __init__(self, x, y, block):
        """
        функция создания блока, создает блок по заданным координатам и виду блока указанного цифрой
        :param x:
        :param y:
        :param block:
        """
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.fon_block = False
        self.poly_block = False
        if block == 1:
            self.image = image.load("%s/textures/block/platform.png" % ICON_DIR)  # каменный блок
        elif block == 2:
            self.image = image.load("%s/textures/block/dirt.png" % ICON_DIR)  # грязь
        elif block == 3:
            self.image = image.load("%s/textures/block/earst.png" % ICON_DIR)  # блок травы
        elif block == 4:
            self.image = image.load("%s/textures/block/stone.png" % ICON_DIR)  # камень
        elif block == 5:
            self.image = image.load("%s/textures/block/pesok.png" % ICON_DIR)  # песок
        elif block == 6:
            self.image = image.load("%s/textures/block/treeeee.png" % ICON_DIR)  # дерево
            self.fon_block = True
        elif block == 7:
            self.image = image.load("%s/textures/decor/stone 1.png" % ICON_DIR)  # диагональный блок травы
            self.poly_block = True
            self.fon_block = True


        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


def add_block(platforms, camera, entities, hero, block_num, npc):
    """
    функция добавленияблоков левой кнопкой мыши
    определяет место блока
    :param platforms:
    :param camera:
    :param entities:
    :param hero:
    :param block_num:
    :param npc:
    :return:
    """
    mouse_pl = mouse.get_pos()
    mouse_pl_click = mouse.get_pressed()
    tmp = -1
    for e in platforms:
        tmp += 1
        if hero.rect.x - 128 < mouse_pl[0] - camera.state.x < hero.rect.x + 128 + hero.rect.w and hero.rect.y - 128 < \
                mouse_pl[1] - camera.state.y < hero.rect.y + 128 + hero.rect.h:
            if e.rect.x < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w:  # block down
                if e.rect.y + e.rect.h < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h * 2:
                    pl_tmp = Rect(e.rect.x, e.rect.y + e.rect.h, e.rect.w, e.rect.h)
                    if mouse_pl_click[2] == 1 and chek_block(pl_tmp, platforms, hero, npc):
                        pl = Platform(e.rect.x, e.rect.y + e.rect.h, block_num)
                        platforms.append(pl)
                        entities.add(pl)

            if e.rect.x < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w:  # block up
                if e.rect.y - e.rect.h < mouse_pl[1] - camera.state.y < e.rect.y:
                    pl_tmp = Rect(e.rect.x, e.rect.y - e.rect.h, e.rect.w, e.rect.h)
                    if mouse_pl_click[2] == 1 and chek_block(pl_tmp, platforms, hero, npc):
                        pl = Platform(e.rect.x, e.rect.y - e.rect.h, block_num)
                        platforms.append(pl)
                        entities.add(pl)

            if e.rect.x - e.rect.w < mouse_pl[0] - camera.state.x < e.rect.x:  # block left
                if e.rect.y < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h:
                    pl_tmp = Rect(e.rect.x - e.rect.w, e.rect.y, e.rect.w, e.rect.h)
                    if mouse_pl_click[2] == 1 and chek_block(pl_tmp, platforms, hero, npc):
                        pl = Platform(e.rect.x - e.rect.w, e.rect.y, block_num)
                        platforms.append(pl)
                        entities.add(pl)

            if e.rect.x + e.rect.w < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w * 2:  # bloc right
                if e.rect.y < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h:
                    pl_tmp = Rect(e.rect.x + e.rect.w, e.rect.y, e.rect.w, e.rect.h)
                    if mouse_pl_click[2] == 1 and chek_block(pl_tmp, platforms, hero, npc):
                        pl = Platform(e.rect.x + e.rect.w, e.rect.y, block_num)
                        platforms.append(pl)
                        entities.add(pl)


def chek_block(pl_tmp, platforms, hero, npc):
    """
    функция проверяет, можно ли поставить блок в данном месте
    :param pl_tmp:
    :param platforms:
    :param hero:
    :param npc:
    :return:
    """
    for pl in platforms:
        if pl_tmp.colliderect(pl) or pl_tmp.colliderect(hero) or pl_tmp.colliderect(npc):
            return False
    return True


def remove_bolck(platforms, camera, entities, hero):
    """
    функция удаляет блоки по нажатию на левую кнопку мыши
    :param platforms:
    :param camera:
    :param entities:
    :param hero:
    :return:
    """
    mouse_pl = mouse.get_pos()
    mouse_pl_click = mouse.get_pressed()
    tmp = -1
    for e in platforms:
        tmp += 1
        if hero.rect.x - 128 < mouse_pl[0] - camera.state.x < hero.rect.x + 128 + hero.rect.w and hero.rect.y - 128 < \
                mouse_pl[1] - camera.state.y < hero.rect.y + 128 + hero.rect.h:
            if e.rect.x < mouse_pl[0] - camera.state.x < e.rect.x + e.rect.w:
                if e.rect.y < mouse_pl[1] - camera.state.y < e.rect.y + e.rect.h:
                    if mouse_pl_click[0] == 1:
                        platforms.pop(tmp)
                        entities.remove(e)
