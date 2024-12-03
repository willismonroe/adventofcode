import solve
from solve import example_input, example_input2


def test_part1():
    assert solve.part1(example_input) == 4
    assert solve.part1(example_input2) == 8


def test_part2():
    assert solve.part2(example_input) == 1
