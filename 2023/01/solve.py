import pathlib
import re

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def part1(input):
    sum = 0
    for line in input.splitlines():
        digit = ""
        for c in line:
            if c.isdigit():
                digit += c
                break
        for c in line[::-1]:
            if c.isdigit():
                digit += c
                break
        sum += int(digit)
    return sum


def convert_num(s: str) -> int:
    match s:
        case "zero":
            return '0'
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
    return 0


def part2(input):
    sum = 0
    for line in input.splitlines():
        digit = ""
        results = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))", line
        )
        if results[0].isdigit():
            digit += results[0]
        else:
            digit += convert_num(results[0])
        if results[-1].isdigit():
            digit += results[-1]
        else:
            digit += convert_num(results[-1])
        sum += int(digit)

    return sum


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
