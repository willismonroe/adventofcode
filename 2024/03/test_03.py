import pathlib
import pytest

from solve_03 import example_input, example_input2
from solve_03 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def puzzle_input():
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    return puzzle_input


def test_part1(puzzle_input):
    assert part1(example_input) == 161
    assert part1(puzzle_input) == 189600467


def test_part2(puzzle_input):
    assert part2(example_input2) == 48
    assert part2(puzzle_input) == 107069718
