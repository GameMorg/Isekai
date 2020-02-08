#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами
 
class Platform(sprite.Sprite):
    def __init__(self, x, y, block):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.fon_block = False
        self.poly_block = False
        if block == 1:
            self.image = image.load("%s/textures/block/platform.jpg" % ICON_DIR)

        elif block == 2:
            self.image = image.load("%s/textures/block/dirt.jpg" % ICON_DIR)
        elif block == 3:
            self.image = image.load("%s/textures/block/earst.jpg" % ICON_DIR)
        elif block == 4:
            self.image = image.load("%s/textures/block/stone.jpg" % ICON_DIR)
        elif block == 5:
            self.image = image.load("%s/textures/block/pesok.jpg" % ICON_DIR)
        elif block == 6:
            self.image = image.load("%s/textures/block/treeeee.png" % ICON_DIR)
            self.fon_block = True
        elif block == 7:
            self.image = image.load("%s/textures/block/land_grass_L.png" % ICON_DIR)
            self.poly_block = True

        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

