class Cursor():
    def __init__(self, block):
        self.map = block

    def place(self, x, y):
        get1 = self.map[y]
        get2 = get1[x]
        return get2

    def set(self, x, y, arg):
        get1 = self.map[y]
        get2 = get1[x]
        get2[x] = arg


class Map_block():
    def __init__(self, x, y, numb):
        r = 0
        self.numb = numb
        self.block = []
        for i in range(x):
            self.block.append([])
            for j in range(y):
                self.block[i].append(r)


def land_cart(chank, max_x, max_y):
    x = 0
    y = 0
    for elem in chank:
        y += 1
        for i in elem:
            x += 1
            if y > max_y:
                elem.pop(x)
                elem.insert(x, 1)
            else:
                pass

            if x >= max_x:
                x = -1

    return chank
