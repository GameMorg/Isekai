import pygame
from save_game import *
from player import *


class Button():
    def __init__(self, widht, height, ineractive_colar=(23, 204, 58), active_color=(13, 162, 58)):
        self.widht = widht
        self.height = height
        self.ineractive_colar = ineractive_colar
        self.active_color = active_color

    def draw(self, x, y, message, win, action=None):
        mosue = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mosue[0] < x + self.widht:
            if y < mosue[1] < y + self.height:
                pygame.draw.rect(win, (23, 204, 58), (x, y, self.widht, self.height))

                if click[0] == 1 and action is not None:
                    pygame.time.delay(300)
                    action()
            else:
                pygame.draw.rect(win, (13, 162, 58), (x, y, self.widht, self.height))
        else:
            pygame.draw.rect(win, (13, 162, 58), (x, y, self.widht, self.height))
        print_text(message, x + 10, y + 10, win)

    def blitx(self, win, image_pas, image_active, x, y, action=None):
        mosue = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mosue[0] < x + self.widht:
            if y < mosue[1] < y + self.height:
                win.blit(image_active, (x, y))

                if click[0] == 1 and action is not None:
                    pygame.time.delay(300)
                    action()
            else:
                win.blit(image_pas, (x, y))
        else:
            win.blit(image_pas, (x, y))


class Block():
    def __init__(self, x, y, num):
        self.width = 32
        self.height = 32
        self.x = x
        self.y = y
        self.num = num
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Camera(object):
    """docstring for Camera"""

    def __init__(self, arg):
        super(Camera, self).__init__()
        self.arg = arg


def chek_collsion(barriers, hero):
    for barrier in barriers:
        if hero.y + hero.height > barrier.y:
            if barrier.x < hero.x < barrier.x + barrier.width:
                return False
            elif barrier.x < hero.x + hero.width < barrier.x + barrier.width:
                return False
    return True


def print_chank(chank, init_block):
    x = 0
    y = 0
    block_arr = []
    for elem in chank:
        for i in elem:
            if i == 1:
                block = 1
                x_b = int(x) * 32
                y_b = int(y) * 32
                block_arr.append(init_block(x_b, y_b, block))
            elif i == 2:
                block = 2
                x_b = int(x) * 32
                y_b = int(y) * 32
                block_arr.append(init_block(x_b, y_b, block))
            elif i == 3:
                block = 3
                x_b = int(x) * 32
                y_b = int(y) * 32
                block_arr.append(init_block(x_b, y_b, block))
            x += 1
            if x >= len(elem):
                x = 0
        y += 1
        if y >= len(chank):
            y = 0
    return block_arr


def main():
    pygame.init()

    save = Save("Save")
    # init display
    display_widht = 800
    display_height = 600
    win = pygame.display.set_mode((display_widht, display_height))
    pygame.display.set_caption("Isekay")

    # init map
    earst = pygame.image.load("textures//block//earst.jpg")
    dirt = pygame.image.load("textures//block//dirt.jpg")
    stone = pygame.image.load("textures//block//stone.jpg")
    chank = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],



    ]

    map_arr = print_chank(chank, Block)

    x = 0
    y = 0
    widht = 32
    height = 64
    speed = 10

    # init mob
    hero = Hero(x, y, speed)
    up = False
    left = False
    right = False

    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #        save.save("hero_x", hero.x)
                run = False

            # e = pygame.key.get_pressed()
            # if keys[pygame.K_a] and hero.x > 10 or \
            #        keys[pygame.K_LEFT] and hero.x > 10:
            #    hero.x_set(-speed)

            # if keys[pygame.K_d] and hero.x < display_widht - 10 - widht or \
            #        keys[pygame.K_RIGHT] and hero.x < display_widht - 10 - widht:
            #    hero.x_set(speed)

            # if keys[pygame.K_F5]:
            #    save.save('x', hero.x)
            #    save.save('hero', hero)

            # if keys[pygame.K_F8]:
            #    hero = save.load('hero')

            # terst

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True

            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                up = False
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False

        win.fill((255, 255, 255))
        # map

        for elem in map_arr:
            block = elem.num
            if block == 1:
                x_b = elem.x
                y_b = elem.y
                win.blit(earst, (x_b, y_b))
            elif block == 2:
                x_b = elem.x
                y_b = elem.y
                win.blit(dirt, (x_b, y_b))
            elif block == 3:
                x_b = elem.x
                y_b = elem.y
                win.blit(stone, (x_b, y_b))
        # hero
        # pygame.draw.rect(win, (0, 0, 255), (hero.x, hero.y, widht, height))
        hero.update(left, right, up, map_arr)
        pygame.display.update()

    pygame.quit()


def print_text(message, x, y, win, font_color=(0, 0, 0), font_type='font_type.otf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))


def menu():
    show = True

    pygame.init()
    # init game

    save = Save("Save")
    meun_backr = pygame.image.load('textures//background//backr.jpg')
    sbp = pygame.image.load('textures//button//load_B2RU.png')
    sba = pygame.image.load("textures//button//Load_BRU.png")
    start_bth = Button(192, 84, sbp, sba)

    display_widht = 800
    display_height = 600
    win = pygame.display.set_mode((display_widht, display_height))
    skale = pygame.transform.scale(meun_backr, (display_widht, display_height))

    # start menu
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

        win.blit(skale, (0, 0))
        start_bth.blitx(win, sbp, sba, display_widht / 2.75, display_height / 6, main)
        pygame.display.update()
