from day09.solve_day09 import part1, part2

example_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""



def test_part1():
    assert part1(example_input) == 15
    assert part1(open('day09_input.txt').read()) == 504


def test_part2():
    assert part2(example_input) == 1134
    # assert part2(open('day10_input.txt').read()) == 986163
