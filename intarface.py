from buttons import *


class Box:
    def __init__(self, num_box):
        self.num_box = num_box
        self.rect = Rect(self.num_box * 40 + 120, 70, 40, 40)
        self.color = (0, 0, 255)

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)


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
    image_bg = image.load("1.jpg")
    image.save(screen, "1.jpg")

    item_box_arr_y = []
    for num_box_y in range(5):
        item_box_arr_x = []
        for num_box_x in range(10):
            item_box = Box(num_box_x)
            item_box.rect.x = (intarface_bg.x + 5) + (item_box.rect.w + 5) * num_box_x
            item_box.rect.y = intarface_bg.y + 45 + (item_box.rect.h + 5) * num_box_y
            item_box_arr_x.append(item_box)
        item_box_arr_y.append(item_box_arr_x)

    intarface_arr_bt = []
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
        for item_box_x in item_box_arr_y:
            for box in item_box_x:
                box.draw(screen)

        display.update()
