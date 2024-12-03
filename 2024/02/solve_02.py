import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def part1(puzzle_input: str) -> int:
    levels = [
        [int(num) for num in line.split()]
        for line in puzzle_input.splitlines()
    ]
    num_safe = 0
    for level in levels:
        safe = True
        diff = 0
        for i, (a, b) in enumerate(zip(level[:-1], level[1:])):
            if i == 0:
                diff = a - b
            else:
                if diff < 0 and a - b > 0:
                    safe = False
                    break
                elif diff > 0 and a - b < 0:
                    safe = False
                    break
            if 1 <= abs(a - b) <= 3:
                safe = True
            else:
                safe = False
                break
        if safe:
            num_safe += 1
    return num_safe


def test_safety(level: list[int]) -> bool:
    safe = True
    diff = 0
    for i, (a, b) in enumerate(zip(level[:-1], level[1:])):
        if i == 0:
            diff = a - b
        else:
            if diff < 0 and a - b > 0:
                safe = False
                break
            elif diff > 0 and a - b < 0:
                safe = False
                break
        if 1 <= abs(a - b) <= 3:
            safe = True
        else:
            safe = False
            break
    return safe


def part2(puzzle_input: str) -> int:
    levels: list[list[int]] = [
        [int(num) for num in line.split()]
        for line in puzzle_input.splitlines()
    ]
    num_safe: int = 0
    for level in levels:
        if test_safety(level):
            num_safe += 1
        else:
            for i, _ in enumerate(level):
                if test_safety(level[0:i] + level[i + 1:]):
                    num_safe += 1
                    break

    return num_safe


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
