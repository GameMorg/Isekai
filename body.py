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
        print_text(message, x + 10, y + 10, win)


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


def main():
    pygame.init()

    save = Save("Save")

    display_widht = 800
    display_height = 600
    win = pygame.display.set_mode((display_widht, display_height))

    pygame.display.set_caption("Isekay")

    x = 100
    y = display_height / 1.3
    widht = 32
    height = 64
    speed = 5

    hero = Hero(x, y, speed)

    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save("hero_x", hero.x)
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and hero.x > 10:
            hero.x_set(-speed)

        if keys[pygame.K_RIGHT] and hero.x < display_widht - 10 - widht:
            hero.x_set(speed)

        win.fill((255, 255, 255))
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

    save = Save("Save")

    BLUE = (0, 0, 255)

    meun_backr = pygame.image.load('textures//backr.jpg')
    start_bth = Button(300, 70, )

    display_widht = 800
    display_height = 600
    win = pygame.display.set_mode((display_widht, display_height))
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

        win.blit(meun_backr, (0, 0))
        start_bth.draw(100, 100, "my first button", win)
        pygame.display.update()
