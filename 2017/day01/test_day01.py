import day01_part1, day01_part2


def test_part1_examples():
    assert day01_part1.solve('1122') == 3
    assert day01_part1.solve('1111') == 4
    assert day01_part1.solve('1234') == 0
    assert day01_part1.solve('91212129') == 9


def test_part1():
    input = open('part1_input.txt').read()
    assert day01_part1.solve(input) == 1203


def test_part2_examples():
    assert day01_part2.solve('1212') == 6
    assert day01_part2.solve('1221') == 0
    assert day01_part2.solve('123425') == 4
    assert day01_part2.solve('123123') == 12
    assert day01_part2.solve('12131415') == 4


def test_part2():
    input = open('part1_input.txt').read()
    assert day01_part2.solve(input) == 1146
