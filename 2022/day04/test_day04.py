import pytest
import solve

example_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_part1():
    assert solve.part1(example_input) == 2


def test_part2():
    assert solve.part2(example_input) == 4
