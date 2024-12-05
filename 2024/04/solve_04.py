import pathlib
from itertools import product

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def get_char(i: int, j: int, grid: list[str]) -> str:
    if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1:
        return grid[i][j]
    else:
        return "."


def part1(puzzle_input: str) -> int:
    grid = puzzle_input.splitlines()
    xs: list[tuple[int, int]] = list()
    xmas_num = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "X":
                xs.append((i, j))
    for i, j in xs:
        for d in [d for d in product([-1, 0, 1], repeat=2) if d != (0, 0)]:
            if get_char(i + d[0], j + d[1], grid) == "M":
                if get_char(i + d[0] * 2, j + d[1] * 2, grid) == "A":
                    if get_char(i + d[0] * 3, j + d[1] * 3, grid) == "S":
                        xmas_num += 1
    return xmas_num


def part2(puzzle_input: str) -> int:
    grid = puzzle_input.splitlines()
    x_mas = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == "A":
                if set((grid[i - 1][j - 1], grid[i + 1][j + 1])) == set(
                    ("M", "S")
                ) and set(
                    (
                        grid[i - 1][j + 1],
                        grid[i + 1][j - 1],
                    )
                ) == set(
                    ("S", "M")
                ):
                    x_mas += 1
    return x_mas


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
