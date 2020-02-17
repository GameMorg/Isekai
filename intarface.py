from buttons import *



class Box:
    def __init__(self, number, screen):
        self.number = number
        self.rect = Rect(0, 0, 40, 40)
        self.image = image.load("textures/block/stone.jpg")
        self.image.transform.sckale()


def interface(screen, display_widht, display_height):
    """
    Функция принимающая значение экрана и заднего фона
    выводит на экран итерфейс игрока, в котором
    1) его инвентарь
    2) его характеристика
    3) его иконка на которую можно нажать и он скажет фразу
    :param screen:
    :return:
    """
    intarface = True
    intarface_bg = Rect(100, 50, display_widht - 100 * 2, display_height - 50 * 2)
    intarface_arr_bt = []
    image.save(screen, "1.jpg")
    image_bg = image.load("1.jpg")



    for i in range(1, 5):
        bt = Rect((intarface_bg.x + 5) * i, intarface_bg.y + 5, 50, 30)
        intarface_arr_bt.append(bt)
    while intarface:
        for e in event.get():
            if e.type == QUIT:
                intarface = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                intarface = False
            if e.type == KEYDOWN and e.key == K_TAB:
                intarface = False
        screen.blit(image_bg, (0, 0))
        draw.rect(screen, (255, 255, 255), intarface_bg)
        for e in intarface_arr_bt:
            draw.rect(screen, (0, 0, 0), e)



        display.update()


def ss():
    """
    функция  для заглушки копки
    :return:
    """
    pass


def item_activete(item):
    item.item = True
