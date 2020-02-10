from buttons import *
import pygame



def settings_menu(hero, screen,  total_level_width, total_level_height, camera, entities):
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
    mose_1 = pygame.mouse.get_pos()
    block_one = entities[0]
    if settings_menu:
        hero_x_message /= 32
        hero_y_message /= 32
        show_time_1 = show_time // 1000
        print_text(str('x = ' + str(hero_x_message)), 0, 0, screen, font_size=20)
        print_text(str('y = ' + str(hero_y_message)), 0, 20, screen, font_size=20)
        print_text(str('time = ' + str(show_time_1) + ' sec'), 0, 40, screen, font_size=20)
        print_text(str('mouse_x = ') + str(mose_1[0]), 0, 60, screen, font_size=20)
        print_text(str('mousr_y = ') + str(mose_1[1]), 0, 80, screen, font_size=20)

        print_text(str('mose_x_level = ') + str(mose_1[0] - camera.state.x), 0, 100, screen, font_size=20)
        print_text(str('mose_y_level = ') + str(mose_1[1] - camera.state.y), 0, 120, screen, font_size=20)

        print_text(str('block_x = ') + str(block_one.rect.x), 0, 140, screen, font_size=20)
        print_text(str('block_y = ') + str(block_one.rect.y), 0, 160, screen, font_size=20)




