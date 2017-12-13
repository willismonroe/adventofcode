import os

import day13_part1, day13_part2

def test_part1_example():
    input = """0: 3
1: 2
4: 4
6: 4""".splitlines()

    assert day13_part1.solve(input) == 24

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day13_input.txt").read().splitlines()

    assert day13_part1.solve(input) == 1632

def test_part2_example():
    input =     input = """0: 3
1: 2
4: 4
6: 4""".splitlines()

    assert day13_part2.solve(input) == 10

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day13_input.txt").read().splitlines()

    assert day13_part2.solve(input) == 3834136