import os

import day13_part1, day13_part2

def test_day13_example():
    input = """0: 3
1: 2
4: 4
6: 4""".splitlines()

    assert day13_part1.solve(input) == 24

def test_day13():
    os.chdir(os.path.dirname(__file__))

    input = open("day13_input.txt").read().splitlines()

    assert day13_part1.solve(input) == 1632