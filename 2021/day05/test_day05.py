import solve

example_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_solve_part1():
    assert solve.part1(example_input) == 5
    assert solve.part1(open('input.txt').read()) == 4421


def test_part2():
    assert solve.part2(example_input) == 12
    assert solve.part2(open('input.txt').read()) == 18674
