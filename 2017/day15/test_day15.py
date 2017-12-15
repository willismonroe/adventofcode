import os

import day15_part1, day15_part2

def test_part1_example():
    input = '65\n8921'.splitlines()

    assert day15_part1.solve(input) == 588

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day15_input.txt").read().splitlines()

    assert day15_part1.solve(input) == 631

def test_part2_example():
    input = '65\n8921'.splitlines()

    assert day15_part2.solve(input) == 309

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day15_input.txt").read().splitlines()

    assert day15_part2.solve(input) == 279