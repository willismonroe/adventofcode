import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def deltas(nums):
    it = iter(nums)
    prev = next(it)

    for n in it:
        yield n - prev
        prev = n


def part1(input):
    # input = example_input
    numbers: list[list[int]] = []
    for line in input.splitlines():
        numbers.append(list(map(int, line.split())))
    # print(numbers)
    # print(list(deltas(deltas(numbers[0]))))
    total = 0
    for nums in numbers:
        while any(nums):
            total += nums[-1]
            nums = list(deltas(nums))

    return total


def part2(input):
    # input = example_input
    numbers: list[list[int]] = []
    for line in input.splitlines():
        numbers.append(list(map(int, line.split())))
    # print(numbers)
    # print(list(deltas(deltas(numbers[0]))))
    total2 = 0
    for nums in numbers:
        total_left = 0
        sign = 1
        while any(nums):
            # total_right += nums[-1]
            total_left += sign * nums[0]
            sign = -sign
            nums = list(deltas(nums))
        total2 += total_left

    return total2


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
