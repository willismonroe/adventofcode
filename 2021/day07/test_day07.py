from day07.solve_day07 import part1, part2

example_input = """16,1,2,0,4,2,7,1,2,14"""


def test_part1():
    assert part1(example_input) == 37
    assert part1(open('input.txt').read()) == 344297


def test_part2():
    assert part2(example_input) == 168
    assert part2(open('input.txt').read()) == 97164301
