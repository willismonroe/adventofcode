import day02_part1, day02_part2

example_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def test_part1_example():
    assert day02_part1.solve(example_input) == 150

def test_part1():
    puzzle_input = open('part1_input.txt').read()
    assert day02_part1.solve(puzzle_input) == 2117664

def test_part2_example():
    assert day02_part2.solve(example_input) == 900

def test_part2():
    puzzle_input = open('part1_input.txt').read()
    assert day02_part2.solve(puzzle_input) == 2073416724