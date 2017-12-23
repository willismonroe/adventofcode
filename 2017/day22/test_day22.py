import os

import day22_part1, day22_part2

def test_part1_example():
    inp = """..#
#..
...""".splitlines()

    assert day22_part1.solve(inp, max_cycles=70) == 41

def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day22_input.txt").read().splitlines()

    assert day22_part1.solve(inp) == 5570

def test_part2_example():
    inp = """..#
    #..
    ...""".splitlines()

    assert day22_part2.solve(inp, max_cycles=100) == 26
    assert day22_part2.solve(inp, max_cycles=10_000_000) == 2511944

def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day22_input.txt").read().splitlines()

    assert day22_part2.solve(inp) == 2512022