# Wrap all button data in a class.
import pygame

class Button(object):
    def __init__(self, x, y, w, h, text, colour=None):
        if colour is None:
            colour = NORMAL

        self.normal_colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = pygame.font.Font(None, 20)
        self.text = text
        self.shiny = False

    def draw(self, screen):
        if self.shiny:
            bg = SHINY
        else:
            bg = self.normal_colour


        BLACK = 255, 255, 255

        surf = self.font.render(self.text, True, BLACK, bg)
        rect = (self.x, self.y, self.w, self.h)
        xo = self.x + (self.w - surf.get_width()) // 2
        yo = self.y + (self.h - surf.get_height()) // 2
        screen.fill(bg, rect)
        screen.blit(surf, (xo, yo))

    def on_button(self, pos):
        return self.x <= pos[0] and self.x + self.w > pos[0] and \
               self.y <= pos[1] and self.y + self.h > pos[1]


# Mouse click handler
def update_click(pos):
    """
    Mouse got clicked
    Returns whether a change occurred.
    """
    global disable_select

    selected_found = None
    selected_set = None
    for elm in buttons:
        if elm.on_button(pos):
            return 