#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame

from player import *
from blocks import *
from menu import *

# Объявляем переменные
WIN_WIDTH = 1920  # Ширина создаваемого окна
WIN_HEIGHT = 1080 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"


class Button():
    def __init__(self, widht, height, ineractive_colar=(23, 204, 58), active_color=(13, 162, 58), save=False, box=False, item=False):
        self.widht = widht
        self.height = height
        self.ineractive_colar = ineractive_colar
        self.active_color = active_color
        self.save = save
        self.click_one = False
        self.box = box
        self.item = item

    def draw(self, x, y, message, win, action=None):
        mosue = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mosue[0] < x + self.widht:
            if y < mosue[1] < y + self.height:
                pygame.draw.rect(win, self.ineractive_colar, (x, y, self.widht, self.height))
                if click[0] == 1 and action is not None:
                    pygame.time.delay(300)
                    if self.click_one:
                        self.click_one = False
                    else:
                        self.click_one = True

                    action()
            else:
                pygame.draw.rect(win, self.active_color, (x, y, self.widht, self.height))
        else:
            pygame.draw.rect(win, self.active_color, (x, y, self.widht, self.height))
        print_text(message, x + 10, y + 10, win)

    def blitx(self, win, image_pas, image_active, x, y, action=None,
              click_sound=mixer.Sound('sounds//environment//mm_button.ogg')):
        mosue = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mixer.pre_init(44100, -16, 1, 512)
        mixer.init()
        if x < mosue[0] < x + self.widht:
            if y < mosue[1] < y + self.height:
                win.blit(image_active, (x, y))

                if click[0] == 1 and action is not None:

                    pygame.time.delay(300)
                    self.click_one = True
                    click_sound.play()
                    if self.save:
                        action(self.save)
                    action()
            else:
                win.blit(image_pas, (x, y))
        else:
            win.blit(image_pas, (x, y))


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


def print_text(message, x, y, win, font_color=(0, 0, 0), font_type='font_type.otf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))


def pause(screen):
    show = True

    while show:
        for e in event.get():
            if e.type == QUIT:
                show = False

            if e.type == KEYDOWN and e.key == K_RETURN:
                show = False

        print_text('Pause, press Enter to continia...', 160, 300, screen)
        display.update()


def interface(screen, bg):
    show = True
    button_hero = Button(200, 75)
    characteristic = Button(200, 75)
    enventory_arr = []
    for i in range(5):
        box_item = Button(30, 30, box=True)
        enventory_arr.append(box_item)

    item = Button(20, 20, active_color=(255, 0, 0), ineractive_colar=(255, 117, 117))

    while show:
        for e in event.get():
            if e.type == QUIT:
                show = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                show = False

        screen.blit(bg, (0, 0))
        button_hero.draw(0, 600 - 75, 'stats', screen, ss)
        if button_hero.click_one:
            characteristic.draw(0, 600 - 150, 'hp = 100/100', screen, ss)
        i = 0
        for e in enventory_arr:
            i += 1
            e.draw(50 * i, 100, '', screen)
            if e.box and i == 1:
                item.draw(50+5, 105, '', screen)

            if i >= len(enventory_arr):
                i = 0

        display.update()


def ss():
    pass


def main(save=False):
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY, FULLSCREEN)  # Создаем окошко
    pygame.display.set_caption("Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    # добавим звуков и музыки
    mixer.pre_init(44100, -16, 1, 512)
    mixer.init()
    shag = mixer.Sound('sounds/music/fon.ogg')
    panche = mixer.Sound('sounds/environment/shag.ogg')
    shag.set_volume(0.3)
    # shag.play(-1)
    old_time = 0
    click_sound = mixer.Sound('sounds//environment//mm_button.ogg')
    #

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    entities.add(hero)

    level = [
        "------------------------------------------------------------------------------------------",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "------                                                                                   -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                                                        -",
        "-                                                        - - - - - - - - - - - - - - - - -",
        "-                                                       ----------------------------------",
        "-                                                       -                                -",
        "-                                                       -                                -",
        "-                                                       -                                -",
        "-                                                       -                                -",
        "-                                                       -*************                   -",
        "-                                                       ------------------------         -",
        "-                                                 t     -                      -         -",
        "-                         d+                      t     -                      --        -",
        "-                        d+**                     t     -                                -",
        "-                       d+****                    t     -                                -",
        "-                      d+******                   t                                      -",
        "-+++++++++++++++++++++++********+++++++++++++++++++++++++++++                            -",
        "------------------------------------------------------------------------------------------"]

    # Sve File
    if save:
        save = Save('Save')
        hero.rect = save.load('rect')
    # load save
    save_new = Save('Save_new')
    # /////
    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
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
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True

            if e.type == KEYUP and e.key == K_w:
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

            if e.type == KEYDOWN and e.key == K_e:
                new_time = time.get_ticks()
                if new_time - old_time > 1000:
                    old_time = new_time
                    panche.play()

            if e.type == KEYDOWN and e.key == K_TAB:
                interface(screen, bg)


        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms)  # передвижение
        # entities.draw(screen) # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    menu()
