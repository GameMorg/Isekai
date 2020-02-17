from buttons import *


class Item:
    def __init__(self, name, x, y):
        self.name = name
        self.item_rect = Rect(x, y, 32, 32)
        self.item_chek = False

    def update(self, screen, box_arr):
        self.mose_pos = mouse.get_pos()
        self.mouse_press = mouse.get_pressed()
        if self.item_rect.x < self.mose_pos[0] < self.item_rect.x + self.item_rect.w and self.item_rect.y < \
                self.mose_pos[1] < self.item_rect.y + self.item_rect.h:
            if self.mouse_press[0] == 1:
                time.delay(60)
                if self.item_chek:
                    self.item_chek = False
                else:
                    self.item_chek = True
        if self.item_chek:
            self.item_rect.x = self.mose_pos[0] - self.item_rect.w / 2
            self.item_rect.y = self.mose_pos[1] - self.item_rect.h / 2
            draw.rect(screen, (23, 204, 58), self.item_rect)
        else:
            draw.rect(screen, (23, 204, 58), self.item_rect)


class Box_item:
    def __init__(self, x, y, nuber):
        self.rect = Rect(x, y, 40, 40)
        self.number = nuber
        self.box_chek = False

    def update(self, items):
        self.mouse_press = mouse.get_pressed()
        for e in items:
            if self.rect.x < e.item_rect.x + e.item_rect.w / 2 < self.rect.x + self.rect.w and \
                    self.rect.y < e.item_rect.y + e.item_rect.h / 2 < self.rect.y + self.rect.h:
                if self.mouse_press[0] == 1:
                    time.delay(60)
                    e.item_rect.x = self.rect.x + 4
                    e.item_rect.y = self.rect.y + 4
                    e.item_chek = False


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
    sword = Item("Sword", 0, 0)
    stone = Item("Stone", 100, 100)
    box_rect = Rect(200, 100, 40, 40)
    #
    box_arr = []
    box = Box_item(100, 200, 1)
    box_arr.append(box)
    #
    items = [sword, stone]

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

        # box
        mose_pos = mouse.get_pos()
        mouse_press = mouse.get_pressed()
        for e in box_arr:
            e.update(items)

        draw.rect(screen, (5, 50, 50), box_rect)
        # item
        sword.update(screen, box_arr)
        stone.update(screen, box_arr)
        display.update()


def ss():
    """
    функция  для заглушки копки
    :return:
    """
    pass


def item_activete(item):
    item.item = True
