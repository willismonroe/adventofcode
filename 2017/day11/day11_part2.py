import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day11_input.txt").read().split(',')

    print(solve(input))


directions = {
    'n':    [0, 1, -1],
    'ne':   [1, 0, -1],
    'se':   [1, -1, 0],
    's':    [0, -1, 1],
    'sw':   [-1, 0, 1],
    'nw':   [-1, 1, 0]
}

def solve(input):
    # current position: x, y, z
    pos = [0, 0, 0]
    max_dist = 0
    for direction in input:
        pos = [a + b for a, b in zip(pos, directions[direction])]
        distance = int((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)
        if distance > max_dist:
            max_dist = distance

    return max_dist

if __name__ == '__main__':
    main()
