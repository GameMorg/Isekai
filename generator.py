import numpy as np


class Mymap():
    def __init__(self, num):
        self.chank_widht = 30
        self.chank_height = 30
        self.chank = np.zeros((self.chank_widht, self.chank_height), dtype=int)
        self.chank_num = num

    def line_y(self, y, number):
        self.chank[y] = number

    def line_x(self, x, number):
        for elem in self.chank:
            for e in range(len(elem)):
                if e == x:
                    elem[x] = number

    def cube(self, x, y, a, number):
        self.a = a
        self.cube_x = x
        self.cube_y = y

        x = y = 0
        for elem in self.chank:
            for e in range(len(elem)):
                if self.cube_x <= x < self.cube_x + a and self.cube_y <= y < self.cube_y + a:
                    elem[e] = number

                x += 1
            y += 1
            x = 0


def chank_mass(n):
    chank = [0]*n
    for i in range(n):
        chank[i] = Mymap(i)
    return chank



if __name__ == '__main__':
    chank = Mymap(1)
    chank.line_y(24, 1)
    chank.line_y(0, 1)
    chank.line_x(0, 1)
    chank.line_x(18, 1)
    chank.cube(19 - 6, 24 - 5, 5, 1)
    print(chank.chank)
