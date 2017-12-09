import os

import day09_part1, day09_part2


def test_part1_example():
    assert day09_part1.solve('{}') == 1
    assert day09_part1.solve('{{{}}}') == 6
    assert day09_part1.solve('{{},{}}') == 5
    assert day09_part1.solve('{{{},{},{{}}}}') == 16
    assert day09_part1.solve('{<a>,<a>,<a>,<a>}') == 1
    assert day09_part1.solve('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert day09_part1.solve('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert day09_part1.solve('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


def test_part1():
    os.chdir(os.path.dirname(__file__))

    input = open("day09_input.txt").read()

    assert day09_part1.solve(input) == 10050


def test_part2_example():
    assert day09_part2.solve('<>') == 0
    assert day09_part2.solve('<random characters>') == 17
    assert day09_part2.solve('<<<<>') == 3
    assert day09_part2.solve('<{!>}>') == 2
    assert day09_part2.solve('<!!>') == 0
    assert day09_part2.solve('<!!!>>') == 0
    assert day09_part2.solve('<{o"i!a,<{i<a>') == 10


def test_part2():
    os.chdir(os.path.dirname(__file__))

    input = open("day09_input.txt").read()

    assert day09_part2.solve(input) == 4482
