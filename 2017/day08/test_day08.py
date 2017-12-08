import os

import day08_part1, day08_part2

def test_part1_example():
    input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".splitlines()

    assert day08_part1.solve(input) == 1

def test_part1():
    os.chdir(os.path.dirname(__file__))

    input = open("day08_input.txt").read().splitlines()

    assert day08_part1.solve(input) == 4877

def test_part2_example():
    input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".splitlines()

    assert day08_part2.solve(input) == 10

def test_part2():
    os.chdir(os.path.dirname(__file__))

    input = open("day08_input.txt").read().splitlines()

    assert day08_part2.solve(input) == 5471
