import solve

example_input = """1721
979
366
299
675
1456"""


def test_part1():
    assert solve.part1(example_input) == 514579
    assert solve.part1(open('day01.txt').read()) == 436404


def test_part2():
    assert solve.part2(example_input) == 241861950
    assert solve.part2(open('day01.txt').read()) == 274879808
