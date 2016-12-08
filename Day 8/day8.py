import numpy as np


class Screen:
    def __init__(self, size_x, size_y):
        self.screen = np.array([['.'] * size_x] * size_y)

    def rect(self, x, y):
        self.screen[0:y, 0:x] = '#'

    def rotate_row(self, row, distance):
        self.screen[row] = np.roll(self.screen[row], distance)

    def rotate_column(self, column, distance):
        self.screen[:, column] = np.roll(self.screen[:, column], distance)

    def count_pixels(self):
        return len(np.argwhere(self.screen == '#'))

    def parse_line(self, line):

        if line[:5] == 'rect ':
            x, y = map(int, line[5:].split('x'))
            self.rect(x, y)

        elif line[:13] == 'rotate row y=':
            row, distance = map(int, line[13:].split(' by '))
            self.rotate_row(row, distance)

        elif line[:16] == 'rotate column x=':
            column, distance = map(int, line[16:].split(' by '))
            self.rotate_column(column, distance)

        else:
            print("Did not understand line: {}".format(line))

    def pprint(self):
        for row in self.screen:
            print(''.join(row))


def solve(screen, data):
    for line in data:
        screen.parse_line(line)
    return screen.count_pixels()


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    screen = Screen(50, 6)
    print(solve(screen, data))
    screen.pprint()
