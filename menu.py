import pygame
from pygame import mixer
from save_game import *
from main import main


class Button():
    def __init__(self, widht, height, ineractive_colar=(23, 204, 58), active_color=(13, 162, 58), save=False):
        self.widht = widht
        self.height = height
        self.ineractive_colar = ineractive_colar
        self.active_color = active_color
        self.save = save

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
                    click_sound.play()
                    if self.save:
                        action(self.save)
                    action()
            else:
                win.blit(image_pas, (x, y))
        else:
            win.blit(image_pas, (x, y))


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
    lbp = pygame.image.load('textures//button//load_B2.png')
    lba = pygame.image.load("textures//button//Load_B.png")

    start_bth = Button(192, 84, sbp, sba)

    load_bth = Button(192, 84, lbp, lba, save=True)

    exit_buttonn = Button(192, 84)


    display_widht = 1920
    display_height = 1080
    win = pygame.display.set_mode((display_widht, display_height), pygame.FULLSCREEN)
    skale = pygame.transform.scale(meun_backr, (display_widht, display_height))


    # start menu
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                show = False




        win.blit(skale, (0, 0))
        start_bth.blitx(win, sbp, sba, display_widht / 2 - 192/2, 100, main)
        load_bth.blitx(win, lbp, lba, display_widht/2 - 192/2, 200, main)
        pygame.display.update()
