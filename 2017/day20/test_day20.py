import os

import day20_part1, day20_part2


def test_part1_example():
    input = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()

    assert day20_part1.solve(input, 4) == 0


def test_part1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day20_input.txt").read().splitlines()

    assert day20_part1.solve(input) == 308


def test_part2_example():
    input = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".splitlines()

    assert day20_part2.solve(input) == 1


def test_part2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day20_input.txt").read().splitlines()

    assert day20_part2.solve(input) == 504
