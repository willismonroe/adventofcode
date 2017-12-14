import os

import day14_part1


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day14_input.txt").read()

    print(solve(input))


def solve(input: str) -> int:
    grid = day14_part1.create_grid(input)

    def get_adjacent(cell: (int, int)):
        y, x = cell
        adjacents = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        adjacents = [adjacent for adjacent in adjacents
                     if 0 <= adjacent[0] < len(grid) and 0 <= adjacent[1] < len(grid[0])]
        return adjacents

    seen = set()

    def dfs(start: (int, int)):
        stack = [start]
        while stack:
            cell = stack.pop()
            y, x = cell
            if grid[y][x] == '.':
                continue
            if cell not in seen:
                seen.add(cell)
                # blank the cell
                # grid[y][x] = '.'
                stack.extend([c for c in get_adjacent(cell) if c not in seen])
        return

    groups = 0

    for y in range(128):
        for x in range(128):
            if (y, x) in seen:
                continue
            if grid[y][x] == ".":
                continue
            groups += 1
            dfs((y, x))

    return groups


if __name__ == '__main__':
    main()
