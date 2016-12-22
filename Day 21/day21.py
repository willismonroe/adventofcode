
from collections import deque
from itertools import permutations

class Scramble:
    def __init__(self, start):
        self.str = list(start)

    def swap_pos(self, x, y):
        self.str[x], self.str[y] = self.str[y], self.str[x]

    def swap_let(self, x, y):
        self.swap_pos(self.str.index(x), self.str.index(y))

    def rotate_left(self, steps):
        steps = steps % len(self.str)
        self.str = self.str[steps:] + self.str[:steps]

    def rotate_right(self, steps):
        steps = steps % len(self.str)
        self.str = self.str[-steps:] + self.str[:-steps]

    def rotate_pos(self, letter):
        steps = self.str.index(letter) + 1
        if steps - 1 >= 4:
            steps += 1
        self.rotate_right(steps)

    def reverse_pos(self, x, y):
        span = self.str[x:y+1]
        self.str[x:y+1] = span[::-1]

    def move_pos(self, x, y):
        letter = self.str.pop(x)
        self.str.insert(y, letter)

    def parse(self, line):
        line = line.split()
        if line[0] == 'swap':
            if line[1] == 'position':
                self.swap_pos(int(line[2]), int(line[5]))
            elif line[1] == 'letter':
                self.swap_let(line[2], line[5])
        elif line[0] == 'rotate':
            if line[1] == 'left':
                self.rotate_left(int(line[2]))
            elif line[1] == 'right':
                self.rotate_right(int(line[2]))
            elif line[1] == 'based':
                self.rotate_pos(line[6])
        elif line[0] == 'reverse':
            self.reverse_pos(int(line[2]), int(line[4]))
        elif line[0] == 'move':
            self.move_pos(int(line[2]), int(line[5]))
        else:
            print("Didn't understand instruction: {}.".format(line))

    def __repr__(self):
        return ''.join(self.str)

    def __eq__(self, other):
        return ''.join(self.str) == other

def solve(start, data):
    scrambler = Scramble(start)
    data = deque(data)
    while data:
        line = data.popleft()
        scrambler.parse(line)
    return scrambler

def solve_v2(start, data):
    for str in permutations(start):
        end = solve(str, data)
        if end == start:
            return ''.join(str)

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    start = 'abcdefgh'

    #with open('test_input.txt') as f:
    #    data = f.read().splitlines()
    #start = 'abcde'

    print("Part 1: {}.".format(solve(start, data)))

    start = 'fbgdceah'
    print("Part 2: {}.".format(solve_v2(start, data)))