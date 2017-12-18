import os

import day18_part1, day18_part2


def test_part1_example():
    input = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".splitlines()

    assert day18_part1.solve(input) == 4


def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day18_input.txt").read().splitlines()

    assert day18_part1.solve(input) == 9423


def test_part2_example():
    input = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""".splitlines()

    assert day18_part2.solve(input) == 3


def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day18_input.txt").read().splitlines()

    assert day18_part2.solve(input) == 7620
