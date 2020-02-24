from buttons import *


class Box:
    def __init__(self, num_box):
        self.num_box = num_box
        self.rect = Rect(self.num_box * 40 + 120, 70, 40, 40)
        self.color = (0, 0, 255)
        self.item = False

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)


class Item:
    def __init__(self, box):
        self.box = box
        self.rect = Rect(self.box.rect.x + 5, self.box.rect.y + 5, self.box.rect.w - 10, self.box.rect.h - 10)
        self.color = (50, 255, 100)
        self.item_mouse = False

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)

    def update(self, mouse_pos, mouse_press, box_arr):
        if self.rect.x < mouse_pos[0] < self.rect.x + self.rect.w and self.rect.y < mouse_pos[
            1] < self.rect.y + self.rect.h:
            self.color = (0, 0, 0)
            if mouse_press[0] == 1:
                for box_y in box_arr:
                    for box_x in box_y:
                        if self.item_mouse and box_x.rect.x < mouse_pos[
                            0] < box_x.rect.x + box_x.rect.w and box_x.rect.y < mouse_pos[
                            1] < box_x.rect.y + box_x.rect.h:
                            self.item_mouse = False
                            self.box = box_x
                        else:
                            self.item_mouse = True

        else:
            self.color = (50, 255, 100)

        if self.item_mouse:
            self.rect.x = mouse_pos[0] - self.rect.w / 2
            self.rect.y = mouse_pos[1] - self.rect.h / 2
        else:
            self.rect.x = self.box.rect.x + 5
            self.rect.x = self.box.rect.y + 5


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

    item_arr = []
    for num in range(5):
        box_y = item_box_arr_y[0]
        box_x = box_y[num]
        item = Item(box_x)
        item_arr.append(item)

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
        mouse_pos = mouse.get_pos()
        mouse_press = mouse.get_pressed()
        for item in item_arr:
            item.update(mouse_pos, mouse_press, item_box_arr_y)
            item.draw(screen)

        display.update()
