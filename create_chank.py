class Chanck():
    def __init__(self):
        self.chanck = [[0] * 19]*25

    def print_chank(self):
        print(self.chanck)


if __name__ == '__main__':
    x = Chanck()
    for elem in x.chanck:
        print(elem)

    y_elem = -1
    for elem in x.chanck:
        y_elem += 1
        for i in range(len(elem)):
            if y_elem > len(x.chanck)/2:
                elem[i] = 1
    print(1)
    for elem in x.chanck:
        print(elem)