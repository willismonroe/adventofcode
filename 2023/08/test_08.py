import solve
from solve import example_input, example_input2, example_input3


def test_part1():
    assert solve.part1(example_input) == 2
    assert solve.part1(example_input2) == 6



def test_part2():
    assert solve.part2(example_input3) == 6
