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

