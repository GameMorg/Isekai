import pygame
from save_game import *


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
    def __init__(self):
        pass

    def draw(self):
        pass


class Hero(object):
    """docstring for Hero"""

    def __init__(self, x, y, speed):
        super(Hero, self).__init__()
        self.x = x
        self.y = y
        self.speed = speed

    def x_set(self, x):
        self.x += x

    def y(self, y):
        self.y += y


class Camera(object):
    """docstring for Camera"""

    def __init__(self, arg):
        super(Camera, self).__init__()
        self.arg = arg


def print_chank(chank, x, y):
    x = 0
    y = 0
    list_map = []
    for elem in chank:
        for i in elem:
            if i == 1:
                block = 1
                x_b = int(x) * 32
                y_b = int(y) * 32
                tmp = [block, x_b, y_b]
                list_map.append(tmp)
            elif i == 2:
                block = 2
                x_b = int(x) * 32
                y_b = int(y) * 32
                tmp = [block, x_b, y_b]
                list_map.append(tmp)
            x += 1
            if x >= len(elem):
                x = 0
        y += 1
        if y >= len(chank):
            y = 0
    return list_map


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
        [],
        [],
        [],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    ]

    # init button
    x = 100
    y = 353
    widht = 32
    height = 64
    speed = 5

    # init mob
    hero = Hero(x, y, speed)

    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save("hero_x", hero.x)
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and hero.x > 10 or\
                keys[pygame.K_LEFT] and hero.x > 10:
            hero.x_set(-speed)

        if keys[pygame.K_d] and hero.x < display_widht - 10 - widht or\
                keys[pygame.K_RIGHT] and hero.x < display_widht - 10 - widht:
            hero.x_set(speed)

        if keys[pygame.K_F5]:
            save.save('x', hero.x)
            save.save('hero', hero)

        if keys[pygame.K_F8]:
            hero = save.load('hero')


        win.fill((255, 255, 255))
        # map
        tmp = print_chank(chank, 25, 19)
        for elem in tmp:
            block = elem[0]
            if block == 1:
                x_b = elem[1]
                y_b = elem[2]
                win.blit(earst, (x_b, y_b))
            elif block == 2:
                x_b = elem[1]
                y_b = elem[2]
                win.blit(dirt, (x_b, y_b))
        # hero
        pygame.draw.rect(win, (0, 0, 255), (hero.x, hero.y, widht, height))
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
