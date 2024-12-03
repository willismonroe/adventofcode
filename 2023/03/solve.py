import pathlib

import re


PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def get_adjacent_cells(x: int, x2: int, y: int):
    """
    Returns a list of adjacent cells to the given coordinates (x, y).

    Args:
        x (int): The starting x-coordinate.
        x2 (int): The ending x-coordinate.
        y (int): The y-coordinate.

    Returns:
        list: A list of adjacent cells as tuples.
    """
    return [
        c
        for c in [
            (i, j) for i in range(x - 1, x2 + 1) for j in range(y - 1, y + 2)
        ]
        if c not in [(i, j) for i in range(x, x2) for j in [y]]
    ]


def part1(input):
    sum = 0
    input = input.splitlines()
    max_x = len(input[0])
    max_y = len(input)
    for y, line in enumerate(input):
        for num in re.finditer(r"\d+", line):
            x, x2 = num.span()
            for cell in get_adjacent_cells(x, x2, y):
                cx, cy = cell
                if 0 < cx < max_x and 0 < cy < max_y:
                    if not input[cy][cx].isdigit():
                        if input[cy][cx] != ".":
                            sum += int(num.group(0))

    return sum


def part2(input):
    ratio = 0
    input: list[str] = input.splitlines()
    # print(f"    {''.join(map(str, range(len(input[0]))))}")
    # for y, line in enumerate(input):
    #     print(f"{y}: ", line)
    parts = []
    for y, line in enumerate(input):
        for num in re.finditer(r"\d+", line):
            x, x2 = num.span()
            parts.append(
                [
                    int(num.group(0)),
                    [(i, j) for i in range(x, x2) for j in [y]],
                ]
            )
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "*":
                adj_parts = []
                adj = [
                    ac
                    for ac in [
                        (i, j)
                        for i in range(x - 1, x + 2)
                        for j in range(y - 1, y + 2)
                    ]
                    if ac != (x, y)
                ]
                # print(x, y, adj)
                for ac in adj:
                    for part in parts:
                        if ac in part[1]:
                            adj_parts.append(part)
                num_parts = list(set([part[0] for part in adj_parts]))
                # print(num_parts)
                if len(num_parts) == 2:
                    # print(x, y, num_parts, num_parts[0] * num_parts[1])
                    ratio += num_parts[0] * num_parts[1]

    return ratio


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
