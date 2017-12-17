import os

import day17_part1, day17_part2


def test_part1_example():
    input = 3

    assert day17_part1.solve(input) == 638


def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = int(open("day17_input.txt").read())

    assert day17_part1.solve(input) == 1306


def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = int(open("day17_input.txt").read())

    assert day17_part2.solve(input) == 20430489
