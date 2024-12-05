import pytest
import solve
from solve import example_input


def test_part1():
    assert solve.part1(example_input) == 26


def test_part2():
    assert solve.part2(example_input) == 1