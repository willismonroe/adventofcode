from day14.solve_day14 import part1, part2

example_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_part1():
    assert part1(example_input) == 1588
    assert part1(open('day14_input.txt').read()) == 2899
#
#
# def test_part2():
#     assert part2(example_input) ==
#     # assert part2(open('day14_input.txt').read()) ==