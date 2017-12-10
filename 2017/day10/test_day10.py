import os

import day10_part1, day10_part2

def test_part1_example():
    input = list(map(int, "3, 4, 1, 5".split(',')))

    assert day10_part1.solve(input, l=list(range(5))) == 12

def test_part1():
    os.chdir(os.path.dirname(__file__))

    input = list(map(int, open("day10_input.txt").read().split(',')))

    assert day10_part1.solve(input) == 62238

def test_part2_example():
    input = ""
    assert day10_part2.solve(input) == "a2582a3a0e66e6e86e3812dcb672a272"
    input = "AoC 2017"
    assert day10_part2.solve(input) == "33efeb34ea91902bb2f59c9920caa6cd"
    input = "1,2,3"
    assert day10_part2.solve(input) == "3efbe78a8d82f29979031a4aa0b16a9d"
    input = "1,2,4"
    assert day10_part2.solve(input) == "63960835bcdc130f0b66d7ff4f6a5a8e"

def test_part2():
    os.chdir(os.path.dirname(__file__))

    input = open("day10_input.txt").read()

    assert day10_part2.solve(input) == "2b0c9cc0449507a0db3babd57ad9e8d8"