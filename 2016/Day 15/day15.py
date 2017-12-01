import re

REGEX = re.compile(r'(\d+) positions|position (\d+)')

class Disc:
    def __init__(self, length, initial):
        self.positions = [0] + [1] * (length - 1)
        self.position = initial

    def open(self, time):
        return self.positions[(self.position + time) % len(self.positions)] == 0

def solve(data):
    discs = []
    for line in data:
        length = int(REGEX.findall(line)[0][0])
        position = int(REGEX.findall(line)[1][1])
        discs.append(Disc(length, position))

    solved = 0
    time = 0
    while not solved:
        release_time = time
        time += 1
        for disc in discs:
            if disc.open(time):
                solved = 1
            else:
                solved = 0
                break
            time += 1

    return release_time

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    print(solve(data))