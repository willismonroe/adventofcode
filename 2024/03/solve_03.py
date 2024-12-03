import pathlib
import re

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""  # noqa

example_input2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""  # noqa


def part1(puzzle_input: str) -> int:
    total = 0
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input):
        total += int(match.split(",")[0][4:]) * int(match.split(",")[1][:-1])
    return total


def part2(puzzle_input: str) -> int:
    total = 0
    do = True
    for match in re.findall(
        r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", puzzle_input
    ):
        if match == "don't()":
            do = False
        elif match == "do()":
            do = True
        elif match[:4] == "mul(" and do:
            total += int(match.split(",")[0][4:]) * int(
                match.split(",")[1][:-1]
            )

    return total


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
