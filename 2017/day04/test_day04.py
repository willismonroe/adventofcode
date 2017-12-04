import day04_part1, day04_part2


def test_part1_example():
    input = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa""".splitlines()
    assert day04_part1.solve(input) == 2


def test_part1():
    input = open("day04_input.txt").read().splitlines()

    assert day04_part1.solve(input) == 466


def test_part2_example():
    assert day04_part2.solve("abcde fghij".splitlines()) == 1
    assert day04_part2.solve("abcde xyz ecdab".splitlines()) == 0
    assert day04_part2.solve("a ab abc abd abf abj".splitlines()) == 1
    assert day04_part2.solve("iiii oiii ooii oooi oooo".splitlines()) == 1
    assert day04_part2.solve("oiii ioii iioi iiio".splitlines()) == 0


def test_part2():
    input = open("day04_input.txt").read().splitlines()

    assert day04_part2.solve(input) == 251
