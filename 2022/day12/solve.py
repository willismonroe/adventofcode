import pathlib
import string
from collections import deque
from math import inf as INFINITY

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def parse_input(inp):
    grid = []
    for line in inp.splitlines():
        grid.append(list(map(lambda c: string.ascii_letters.index(c), line)))
    return grid

def get_neighbors(grid, r, c, h, w):
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < h and 0 <= nc < w:
            yield nr, nc

def get_neighbors_up(grid, r, c, h, w):
    max_el = grid[r][c] + 1
    neighbors = get_neighbors(grid, r, c, h, w)

    for nr, nc in neighbors:
        if grid[nr][nc] <= max_el:
            yield nr, nc

def get_neighbors_down(grid, r, c, h, w):
    min_el = grid[r][c] - 1
    neighbors = get_neighbors(grid, r, c, h, w)

    for nr, nc in neighbors:
        if grid[nr][nc] >= min_el:
            yield nr, nc

def bfs(grid, src, dest, neighbor_function):
    height, width = len(grid), len(grid[0])
    queue = deque([(0, src)])  # distance from src, src
    visited = set()

    while queue:
        distance, rc = queue.popleft()
        r, c = rc

        if rc == dest or grid[r][c] == dest:
            return distance

        if rc not in visited:
            visited.add(rc)

            for neighbor in neighbor_function(grid, r, c, height, width):
                if neighbor in visited:
                    continue

                queue.append((distance + 1, neighbor))


START, END, LOWEST, HIGHEST = 44, 30, 0, 25

def part1(input):
    grid = parse_input(input)
    src = dest = None
    
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == START:
                src = r, c
                grid[r][c] = LOWEST
            elif cell == END:
                dest = r, c
                grid[r][c] = HIGHEST
        if src and dest:
            break
    
    min_dist = bfs(grid, src, dest, get_neighbors)
    return min_dist


def part2(input):
    grid = parse_input(input)
    src = dest = None
    
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == START:
                src = r, c
                grid[r][c] = LOWEST
            elif cell == END:
                dest = r, c
                grid[r][c] = HIGHEST
        if src and dest:
            break
    
    min_dist = bfs(grid, dest, LOWEST, get_neighbors_down)
    return min_dist


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
