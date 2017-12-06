import day06_part1, day06_part2


def test_part1_example():
    input = [0, 2, 7, 0]

    assert day06_part1.solve(input) == 5


def test_part1():
    input = list(map(int, open("day06_input.txt").read().split('\t')))

    assert day06_part1.solve(input) == 6681


def test_part2_example():
    input = [0, 2, 7, 0]

    assert day06_part2.solve(input) == 4


def test_part2():
    input = list(map(int, open("day06_input.txt").read().split('\t')))

    assert day06_part2.solve(input) == 2392
