from day12.solve_day12 import part1, part2

example_input1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

example_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example_input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def test_part1():
    assert part1(example_input1) == 10
    assert part1(example_input2) == 19
    assert part1(example_input3) == 226
    assert part1(open('day12_input.txt').read()) == 3450


def test_part2():
    assert part2(example_input1) == 36
    assert part2(example_input2) == 103
    assert part2(example_input3) == 3509
#     assert part2(open('day14_input.txt').read()) == 2995077699
