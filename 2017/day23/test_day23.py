import os

import day23_part1, day23_part2

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day23_input.txt").read().splitlines()

    assert day23_part1.solve(inp) == 3025

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day23_input.txt").read().splitlines()

    assert day23_part2.solve(inp) == 915