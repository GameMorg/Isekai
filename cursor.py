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



