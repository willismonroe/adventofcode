import pathlib
import string

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse_input(input):
    lines = input.splitlines()
    pairs = []
    for line in lines:
        p1, p2 = [sec.split('-') for sec in line.split(",")]
        p1 = range(int(p1[0]), int(p1[1])+1)
        p2 = range(int(p2[0]), int(p2[1])+1)
        pairs.append([set(p1), set(p2)])
    return pairs


def part1(input):
    pairs = parse_input(input)
    contain = 0
    for pair in pairs:
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            contain += 1
    return contain


def part2(input):
    pairs = parse_input(input)
    overlap = 0
    for pair in pairs:
        if any(pair[0] & pair[1]):
            overlap += 1
    return overlap


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
