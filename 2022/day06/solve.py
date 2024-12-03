import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


def part1(input):
    for i in range(4, len(input)):
        if len(set(input[i-4:i])) == 4:
            return i
    return 0

def part2(input):
    for i in range(14, len(input)):
        if len(set(input[i-14:i])) == 14:
            return i
    return 0


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
