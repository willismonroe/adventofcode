import pathlib
import string

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse_input(input):
    compartments = []
    for bag in input.splitlines():
        l = len(bag) // 2
        p1, p2 = bag[:l], bag[l:]
        compartments.append((p1, p2))
    return compartments


def split(list, chunk):
    for i in range(0, len(list), chunk):
        yield list[i : i + chunk]


def part1(input):
    compartments = parse_input(input)
    errors = []
    for p1, p2 in compartments:
        errors.append("".join(set(p1).intersection(p2)))
    score = 0
    for error in errors:
        score += string.ascii_letters.index(error) + 1
    return score


def part2(input):
    groups = split(input.splitlines(), 3)
    score = 0
    for group in groups:
        badge = "".join((set(group[0]).intersection(group[1]).intersection(group[2])))
        score += string.ascii_letters.index(badge) + 1
    return score


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
