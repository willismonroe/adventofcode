import pytest
import solve

example_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_part1():
    assert solve.part1(example_input) == "CMZ"


def test_part2():
    assert solve.part2(example_input) == "MCD"