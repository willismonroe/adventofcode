import pathlib

# from operator import mul, add
from itertools import product

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# class Node:
#     def __init__(self, value) -> None:
#         self.l = None
#         self.r = None
#         self.value = value

OPERATORS = ["+", "*"]


def part1(puzzle_input: str) -> int:
    valid = 0
    for line in puzzle_input.splitlines():
        target, nums = line.split(maxsplit=1)
        target = int(target[:-1])
        nums = ("(" * (len(nums.split()) - 1)) + nums.replace(" ", ") {} ")
        # print(target, nums)
        for perm in product(OPERATORS, repeat=nums.count("{}")):
            # print(nums.format(*perm), "=", eval(nums.format(*perm)))
            if eval(nums.format(*perm)) == target:
                # print("***", nums.format(*perm), "=", target)
                valid += target
                break

    return valid


def part2(puzzle_input: str) -> int:
    return True


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
