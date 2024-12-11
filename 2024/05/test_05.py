import pathlib
import pytest

from solve_05 import example_input
from solve_05 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def puzzle_input():
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    return puzzle_input


def test_part1(puzzle_input: str):
    assert part1(example_input) == 143
    assert part1(puzzle_input) == 5509


def test_part2(puzzle_input: str):
    assert part2(example_input) == 123
    assert part2(puzzle_input) == 4407
