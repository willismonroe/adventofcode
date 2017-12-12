import os

import day12_part1, day12_part2


def test_part1_example():
    input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".splitlines()

    assert day12_part1.solve(input) == 6


def test_part1():
    os.chdir(os.path.dirname(__file__))

    input = open("day12_input.txt").read().splitlines()

    assert day12_part1.solve(input) == 128

def test_part2_example():
    input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".splitlines()

    assert day12_part2.solve(input) == 2

def test_part2():
    os.chdir(os.path.dirname(__file__))

    input = open("day12_input.txt").read().splitlines()

    assert day12_part2.solve(input) == 209