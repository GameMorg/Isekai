from buttons import *


def settings_menu(hero, screen,  total_level_width, total_level_height):
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
        print_text(str('level_widht = ') + str(total_level_width/32), 0, 90, screen)
        print_text(str('level_height = ') + str(total_level_height / 32), 0, 120, screen)
