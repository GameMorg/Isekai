from pygame import *
import pygame


class Button():
    def __init__(self, widht, height, ineractive_colar=(23, 204, 58), active_color=(13, 162, 58), save=False, box=False,
                 item=False):
        """
        класс кнопка, принимающий значения ширины и высоты
        дополнительно она может принять значеия бокса, предмета, сохранения
        :param widht:
        :param height:
        :param ineractive_colar:
        :param active_color:
        :param save:
        :param box:
        :param item:
        """
        self.widht = widht
        self.height = height
        self.ineractive_colar = ineractive_colar
        self.active_color = active_color
        self.save = save
        self.click_one = False
        self.box = box
        self.item = item

    def draw(self, x, y, message, win, action=None):
        """
        функция рисования кнопки, принимает позицию кнопки по x и y, надпись на кнопке, окно и действие.
        рисует на экране кнопку, а на кнопке сообщениее, у кнопки есть два состаяния:
        пассивное - на кнопке нет курсора
        активное - на кнопке находиться курсор
        если нажать на кнопку, то произойдет действие
        :param x:
        :param y:
        :param message:
        :param win:
        :param action:
        :return:
        """
        # inventory
        self.box = False
        self.item = False
        self.box_item = False
        #
        mosue = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mosue[0] < x + self.widht:
            if y < mosue[1] < y + self.height:
                pygame.draw.rect(win, self.ineractive_colar, (x, y, self.widht, self.height))
                if click[0] == 1 and action is not None:
                    pygame.time.delay(300)
                    #
                    if self.click_one:
                        self.click_one = False  # activate button
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
        """
        функция рисования кнопки, принимает позицию кнопки по x и y, картинку, окно и действие.
        рисует на экране кнопку, с помощью картинки, у кнопки есть два состаяния:
        пассивное - на кнопке нет курсора
        активное - на кнопке находиться курсор
        если нажать на кнопку, то произойдет действие
        :param win:
        :param image_pas:
        :param image_active:
        :param x:
        :param y:
        :param action:
        :param click_sound:
        :return:
        """
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


def print_text(message, x, y, win, font_color=(0, 0, 0), font_type='font_type.ttf', font_size=30):
    """
    функция принимает координаты, текст(его цвет, шрифт и размер)
    печатает на экране текст по координатам
    :param message:
    :param x:
    :param y:
    :param win:
    :param font_color:
    :param font_type:
    :param font_size:
    :return:
    """
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
