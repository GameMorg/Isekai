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
        if block == "-":
            self.image = image.load("%s/textures/block/platform.jpg" % ICON_DIR)
        elif block == "+":
            self.image = image.load("%s/textures/block/dirt.jpg" % ICON_DIR)
        elif block == "*":
            self.image = image.load("%s/textures/block/earst.jpg" % ICON_DIR)
        elif block == "/":
            self.image = image.load("%s/textures/block/stone.jpg" % ICON_DIR)

        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
