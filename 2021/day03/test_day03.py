import part1, part2

example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def test_part1_example():
    assert part1.solve(example_input) == 198

# def test_part1():
#     puzzle_input = open('part1_input.txt').read()
#     assert part1.solve(puzzle_input) == 2117664

def test_part2_example():
    assert part2.solve(example_input) == 230

# def test_part2():
#     puzzle_input = open('part1_input.txt').read()
#     assert part2.solve(puzzle_input) == 2073416724