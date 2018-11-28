import os

import day24_part1, day24_part2

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day24_input.txt").read().splitlines()

    assert day24_part1.solve(inp) == 3025

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day24_input.txt").read().splitlines()

    assert day24_part2.solve(inp) == 915