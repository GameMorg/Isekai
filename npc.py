from buttons import *
import pyganim
import os

# sound
mixer.pre_init(44100, -16, 1, 512)
mixer.init()

#


MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 5.25
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/mario/chaster_1.png' % ICON_DIR),
                   ('%s/mario/chaster_2.png' % ICON_DIR),
                   ('%s/mario/chaster_3.png' % ICON_DIR),
                   ('%s/mario/chaster_4.png' % ICON_DIR),
                   ('%s/mario/chaster_5.png' % ICON_DIR),
                   ('%s/mario/chaster_6.png' % ICON_DIR),
                   ('%s/mario/chaster_7.png' % ICON_DIR),
                   ('%s/mario/chaster_8.png' % ICON_DIR)]

ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
                  ('%s/mario/l2.png' % ICON_DIR),
                  ('%s/mario/l3.png' % ICON_DIR),
                  ('%s/mario/l4.png' % ICON_DIR),
                  ('%s/mario/l5.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, 0.1)]


class Npc(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms, hero, screen, camera, display_widht=1280, display_height=720):
        """
        функция, проверяющее положения нпс, его действия и события
        :param left:
        :param right:
        :param up:
        :param platforms:
        :param hero:
        :param screen:
        :param camera:
        :return:
        """
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))

            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

        self.mouse_pos = mouse.get_pos()  # где находится мышка
        self.mouse_click = mouse.get_pressed()  # какая кнопка нажата

        if self.rect.x - 100 < hero.rect.x < self.rect.x + 100 and \
                self.rect.y - 100 < hero.rect.y < self.rect.y + 100:  # проверяем, находится ли нпс блиско к гг

            self.message_npc("Привет!", screen, camera)
            if self.rect.x < self.mouse_pos[  # check press gg on npc
                0] - camera.state.x < self.rect.x + self.rect.w and self.rect.y < \
                    self.mouse_pos[1] - camera.state.y < self.rect.y + self.rect.h and self.mouse_click[0] == 1:
                self.dialog(screen, display_widht, display_height)

    def collide(self, xvel, yvel, platforms):
        """
        функция проверяет, столкнулся ли нпс с другим обьектом с помощья силы персонажа и препядствий
        :param xvel:
        :param yvel:
        :param platforms:
        :return:
        """
        for p in platforms:
            if sprite.collide_rect(self, p) and not p.fon_block:  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз

                    self.onGround = True  # и становится на что-то твердое
                    # if self.yvel > 10:
                    # self.panche.play()
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def message_npc(self, message, screen, camera, font_color=(0, 0, 0), font_type='font_type.ttf', font_size=15):
        """
        функция, вызывающая над нпс текст
        :param message:
        :param screen:
        :param camera:
        :param font_color:
        :param font_type:
        :param font_size:
        :return:
        """
        font_type = font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        backgroung_message = Rect(self.rect.x + camera.state.x - font_size,
                                  self.rect.y + camera.state.y - font_size * 2.5,
                                  len(message) * font_size, font_size * 2)
        draw.rect(screen, (255, 255, 255), backgroung_message)
        screen.blit(text, (self.rect.x + camera.state.x, self.rect.y + camera.state.y - font_size * 2))

    def dialog(self, screen, display_widht, display_height):
        """
        функция диалога с нпс
        :return:
        """
        # init dialog
        timer = time.Clock()
        dialog = True
        # button dialog
        self.bt_1 = Button(70, 70)
        self.bt_2 = Button(70, 70)
        self.bt_3 = Button(70, 70)
        self.bt_4 = Button(70, 70)
        while dialog:
            timer.tick(60)
            for e in event.get():
                if e.type == QUIT:
                    dialog = False
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    dialog = False
                if e.type == KEYDOWN and e.key == K_TAB:
                    dialog = False
            background_dialog = Rect(display_widht / 4, display_height / 8, display_widht / 2, display_height / 1.3)
            draw.rect(screen, (255, 255, 255), background_dialog)
            self.bt_1.draw(display_widht / 4 + 25, display_height / 1.3 - 25, 'Ох', screen)
            self.bt_2.draw(display_widht / 4 + 25 * 2 + self.bt_1.widht, display_height / 1.3 - 25, 'Ой!', screen)
            self.bt_3.draw(display_widht / 4 + 25 * 3 + self.bt_1.widht * 2, display_height / 1.3 - 25, '...', screen)
            self.bt_4.draw(display_widht / 4 + 25 * 4 + self.bt_1.widht * 3, display_height / 1.3 - 25, 'А?', screen)
            display.update()
