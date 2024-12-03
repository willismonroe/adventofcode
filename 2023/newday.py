#!/usr/bin/python3
import sys
import os
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent

input_template = """"""

solve_template = """import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = \"\"\"\"\"\"


def part1(input):
    return 0


def part2(input):
    return 0


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
"""

tests_template = """import solve
from solve import example_input


def test_part1():
    assert solve.part1(example_input) == 1


def test_part2():
    assert solve.part2(example_input) == 1
"""


def main(day):
    (CURRENT_DIR / day).mkdir(parents=True, exist_ok=False)
    d = pathlib.Path(day)
    input_file = d / "input.txt"
    with input_file.open("w") as f:
        f.write(input_template)
    solve_file = d / "solve.py"
    with solve_file.open("w") as f:
        f.write(solve_template)
    tests_file = d / f"test_{day}.py"
    with tests_file.open("w") as f:
        f.write(tests_template)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
