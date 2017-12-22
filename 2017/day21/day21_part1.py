import os

import numpy as np


from collections import defaultdict


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day21_input.txt").read().splitlines()

    print(solve(inp))


starting_image = [
    ['.','#','.'],
    ['.','.','#'],
    ['#','#','#']
]

class Grid:
    def __init__(self, line):
        self.in_lines = [[c for c in g] for g in line.split(' => ')[0].split('/')]
        self.out_lines = [[c for c in g] for g in line.split(' => ')[1].split('/')]
        self.len = len(self.in_lines)

    def compare(self, grid):
        same = False
        for line1, line2 in zip(grid, self.in_lines):
            if line1 == line2:
                same = True
        return same


def get_size(matrix):
    if len(matrix) % 2 == 0:
        return 2
    elif len(matrix) % 3 == 0:
        return 3


def print_grid(grid):
    for line in grid:
        print_line = ''
        for c in line:
            print_line += c
        print(print_line)
    print('\n')

def solve(inp):
    grids = defaultdict(list)
    for line in inp:
        g = Grid(line)
        grids[g.len].append(g)

    def find_match(grid):
        grid = np.array(grid)
        rotations = [grid.tolist(), np.rot90(grid).tolist(),
                     np.rot90(grid, 2).tolist(), np.rot90(grid, 3).tolist()]
        length = len(grid)
        matches = grids[length]
        for match in matches:
            if match.in_lines in rotations:
                return match.out_lines

        print("No match found...")

    g = starting_image

    iterations = 0
    while iterations < 5:
        print(f"Iteration: {iterations}")
        print_grid(g)
        if len(g) // 2 > 1 and len(g) % 2 == 0:
            pass
        elif len(g) // 3 > 1 and len(g) % 3 == 0:
            pass

        g = find_match(g)


        iterations += 1
    return


if __name__ == '__main__':
    main()
