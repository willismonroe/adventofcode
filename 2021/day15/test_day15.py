from solve_day15 import part1, part2

example_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_part1():
    assert part1(example_input) == 40
    assert part1(open('day15_input.txt').read()) == 537


def test_part2():
     assert part2(example_input) == 315
     assert part2(open('day15_input.txt').read()) == 2881
