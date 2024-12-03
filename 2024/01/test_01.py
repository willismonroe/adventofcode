import pathlib
import pytest

from solve_01 import example_input
from solve_01 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def puzzle_input():
    with open(PUZZLE_DIR / "input.txt") as f:
        puzzle_input = f.read()
    return puzzle_input


def test_part1(puzzle_input):
    assert part1(example_input) == 11
    assert part1(puzzle_input) == 2176849


def test_part2(puzzle_input):
    assert part2(example_input) == 31
    assert part2(puzzle_input) == 23384288
