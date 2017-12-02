import day02_part1
import day02_part2


def test_part1_example():
    raw_input = """5 1 9 5
    7 5 3
    2 4 6 8"""
    input = [[int(item) for item in line.split()] for line in raw_input.split('\n')]
    assert day02_part1.solve(input) == 18


def test_part1():
    input = [[int(item) for item in line.strip('\n').split('\t')] for line in open("day02_input.txt").readlines()]
    assert day02_part1.solve(input) == 32020


def test_part2_example():
    raw_input = """5 9 2 8
    9 4 7 3
    3 8 6 5"""
    input = [[int(item) for item in line.split()] for line in raw_input.split('\n')]
    assert day02_part2.solve(input) == 9


def test_part2():
    input = [[int(item) for item in line.strip('\n').split('\t')] for line in open("day02_input.txt").readlines()]
    assert day02_part2.solve(input) == 236
