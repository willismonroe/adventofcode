import os


# https://stackoverflow.com/questions/15297834/infinite-board-conways-game-of-life-python

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day22_input.txt").read().splitlines()

    print(solve(inp))


def solve(inp, max_cycles=10_000_000):
    grid = {}
    dim = len(inp[0]) // 2
    for line, y in zip(inp, range(-dim, dim + 1)):
        for c, x in zip(line, range(-dim, dim + 1)):
            grid[(x, y)] = 'infected' if c == '#' else 'clean'

    pos = [0, 0]
    facing = 0
    cycle = 0
    infected = 0
    while cycle < max_cycles:
        node = grid[tuple(pos)]
        # turn
        if node == 'clean':
            facing = (facing - 1) % 4
        elif node == 'infected':
            facing = (facing + 1) % 4
        elif node == 'flagged':
            facing = (facing + 2) % 4

        # convert
        if node == 'clean':
            grid[tuple(pos)] = 'weakened'
        elif node == 'weakened':
            grid[tuple(pos)] = 'infected'
            infected += 1
        elif node == 'infected':
            grid[tuple(pos)] = 'flagged'
        elif node == 'flagged':
            grid[tuple(pos)] = 'clean'

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
            grid[tuple(pos)] = 'clean'

        cycle += 1

    return infected


if __name__ == '__main__':
    main()
