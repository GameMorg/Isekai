from buttons import *

# Объявляем переменные
WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"

def interface(screen, bg):
    show = True
    button_hero = Button(200, 75)
    characteristic = Button(200, 75 * 5)
    enventory_arr = []
    for i in range(5):
        box_item = Button(30, 30, box=True)
        enventory_arr.append(box_item)

    item1 = Button(20, 20, active_color=(255, 0, 0), ineractive_colar=(255, 117, 117))

    while show:
        for e in event.get():
            if e.type == QUIT:
                show = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                show = False

        screen.blit(bg, (0, 0))
        button_hero.draw(0, WIN_HEIGHT - 75, 'stats', screen, ss)
        if button_hero.click_one:
            characteristic.draw(0, WIN_HEIGHT - button_hero.height - characteristic.height, str('hp=100/100'), screen,
                                ss)
            print_text(' mp=100/100', 0, WIN_HEIGHT - button_hero.height - characteristic.height + 75, screen)
        i = 0
        for e in enventory_arr:
            i += 1
            e.draw(50 * i, 100, '', screen)
            if e.box and i == 1:
                pass

            if i >= len(enventory_arr):
                i = 0
        x, y = mouse.get_pos()
        if item1.item:
            item1.draw(x, y, '', screen)
        else:
            item1.draw(50 + 5, 105, '', screen, item_activete(item1))
        display.update()

def ss():
    pass

def item_activete(item):
    item.item = True

