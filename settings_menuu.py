from buttons import *
from blocks import *


def settings_menu(hero, screen, block_num):
    """
    функция  принимающая значения экрана и героя
    выводит на экран позицию героя, и время в игре
    :param hero:
    :param screen:
    :return:
    """
    hero_x_message = hero.rect.x
    hero_y_message = hero.rect.y
    show_time = time.get_ticks()

    if settings_menu:
        hero_x_message /= 32
        hero_y_message /= 32
        show_time_1 = show_time // 1000
        print_text(str('x = ' + str(hero_x_message)), 0, 0, screen)
        print_text(str('y = ' + str(hero_y_message)), 0, 30, screen)
        print_text(str('time = ' + str(show_time_1) + ' sec'), 0, 60, screen)
        print_text(str(block_num), 0, 90, screen)
