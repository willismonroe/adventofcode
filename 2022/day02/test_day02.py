import pytest
import solve

example_input = """A Y
B X
C Z"""


def test_part1():
    assert solve.part1(example_input) == 15


def test_part2():
    assert solve.part2(example_input) == 12
