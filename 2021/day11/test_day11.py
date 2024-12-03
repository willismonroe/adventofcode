from day11.solve_day11 import part1, part2

example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_part1():
    assert part1(example_input) == 1656
    assert part1(open('day11_input.txt').read()) == 1683


def test_part2():
    assert part2(example_input) == 195
#     assert part2(open('day14_input.txt').read()) == 2995077699
