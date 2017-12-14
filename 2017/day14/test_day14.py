import os

import day14_part1, day14_part2

def test_part1_example():
    input = 'flqrgnkx'

    assert day14_part1.solve(input) == 8108

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day14_input.txt").read()

    assert day14_part1.solve(input) == 8140

def test_part2_example():
    input = 'flqrgnkx'

    assert day14_part2.solve(input) == 1242

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day14_input.txt").read()

    assert day14_part2.solve(input) == 1182