import solve

example_input = """3,4,3,1,2"""


def test_solve_part1():
    assert solve.part1(example_input) == 5934
    assert solve.part1(open('input.txt').read()) == 360761


def test_part2():
    assert solve.part2(example_input) == 26984457539
    assert solve.part2(open('input.txt').read()) == 1632779838045
