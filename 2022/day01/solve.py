import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def count_elves(input):
    lines = input.splitlines()
    elves = []
    count = 0
    for line in lines:
        if line == "":
            elves.append(count)
            count = 0
        else:
            count += int(line)
    elves.append(count)
    return elves


def part1(input):
    elves = count_elves(input)
    return max(elves)


def part2(input):
    elves = count_elves(input)
    elves.sort(reverse=True)
    return sum(elves[:3])


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
