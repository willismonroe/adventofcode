import day05_part1, day05_part2


def test_part1_example():
    input = list(map(int, """0
3
0
1
-3""".splitlines()))

    assert day05_part1.solve(input) == 5


def test_part1():
    input = list(map(int, open("day05_input.txt").read().splitlines()))

    assert day05_part1.solve(input) == 387096


def test_part2_example():
    input = list(map(int, """0
    3
    0
    1
    -3""".splitlines()))

    assert day05_part2.solve(input) == 10


def test_part2():
    input = list(map(int, open("day05_input.txt").read().splitlines()))

    assert day05_part2.solve(input) == 28040648
