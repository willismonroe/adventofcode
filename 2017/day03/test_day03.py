import day03_part1

def test_part1_example():
    assert day03_part1.solve(1) == 0
    assert day03_part1.solve(12) == 3
    assert day03_part1.solve(23) == 2
    assert day03_part1.solve(1024) == 31

def test_part1():
    assert day03_part1.solve(289326) == 419