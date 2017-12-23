import os


# https://stackoverflow.com/questions/15297834/infinite-board-conways-game-of-life-python

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day22_input.txt").read().splitlines()

    print(solve(inp))


def solve(inp, max_cycles=10000):
    grid = {}
    dim = len(inp[0]) // 2
    for line, y in zip(inp, range(-dim, dim + 1)):
        for c, x in zip(line, range(-dim, dim + 1)):
            grid[(x, y)] = True if c == '#' else False

    pos = [0, 0]
    facing = 0
    cycle = 0
    infected = 0
    while cycle < max_cycles:
        if grid[tuple(pos)] is True:
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4

        if grid[tuple(pos)] is not True:
            grid[tuple(pos)] = True
            infected += 1
        else:
            grid[tuple(pos)] = False

        # move
        if facing == 0:
            pos[1] -= 1
        elif facing == 1:
            pos[0] += 1
        elif facing == 2:
            pos[1] += 1
        elif facing == 3:
            pos[0] -= 1

        # add node if missing
        if tuple(pos) not in grid.keys():
            grid[tuple(pos)] = False

        cycle += 1

    return infected


if __name__ == '__main__':
    main()
