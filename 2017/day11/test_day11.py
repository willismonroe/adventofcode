import os

import day11_part1, day11_part2

def test_part1_example():
    input = "ne,ne,ne".split(',')
    assert day11_part1.solve(input) == 3
    input = "ne,ne,sw,sw".split(',')
    assert day11_part1.solve(input) == 0
    input = "ne,ne,s,s".split(',')
    assert day11_part1.solve(input) == 2
    input = "se,sw,se,sw,sw".split(',')
    assert day11_part1.solve(input) == 3

def test_part1():
    os.chdir(os.path.dirname(__file__))

    input = open("day11_input.txt").read().split(',')

    assert day11_part1.solve(input) == 743

def test_part2():
    os.chdir(os.path.dirname(__file__))

    input = open("day11_input.txt").read().split(',')

    assert day11_part2.solve(input) == 1493