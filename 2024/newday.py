#!/usr/bin/python3
import sys
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent

input_template = """"""

solve_template = """import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = \"\"\"\"\"\"


def part1(puzzle_input: str) -> int:
    return True


def part2(puzzle_input: str) -> int:
    return True


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
"""


def tests_template(day):
    return f"""import pathlib
import pytest

from solve_{day} import example_input
from solve_{day} import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def puzzle_input():
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    return puzzle_input


def test_part1(puzzle_input: str):
    assert part1(example_input) == 0
    # assert part1(puzzle_input) == 0


def test_part2(puzzle_input: str):
    assert part2(example_input) == 0
    # assert part2(puzzle_input) == 0
"""


def main(day):
    (CURRENT_DIR / day).mkdir(parents=True, exist_ok=False)
    d = pathlib.Path(day)
    input_file = d / "puzzle_input.txt"
    with input_file.open("w") as f:
        f.write(input_template)
    solve_file = d / f"solve_{day}.py"
    with solve_file.open("w") as f:
        f.write(solve_template)
    tests_file = d / f"test_{day}.py"
    with tests_file.open("w") as f:
        f.write(tests_template(day))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("./newday.py two-digit-day")
