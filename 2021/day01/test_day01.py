import day01_part1, day01_part2

example_input = """199
200
208
210
200
207
240
269
260
263"""

def test_part1_example():
    assert day01_part1.solve(example_input) == 7

def test_part1():
    puzzle_input = open('part1_input.txt').read()
    assert day01_part1.solve(puzzle_input) == 1676

def test_part2_example():
    assert day01_part2.solve(example_input) == 5

print(day01_part2.solve(example_input))