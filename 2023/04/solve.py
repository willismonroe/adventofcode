import pathlib
from math import pow

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def part1(input: str):
    # input = example_input
    sum = 0
    for line in input.splitlines():
        w_nums, nums = line.split("|")
        w_nums = w_nums.split(":")[1]
        w_nums = list(map(int, w_nums.split()))
        nums = list(map(int, nums.split()))
        if len(set(w_nums) & set(nums)) > 0:
            sum += int(pow(2, len(set(w_nums) & set(nums)) - 1))
    return sum


def part2(input):
    # input = example_input
    cards = []
    for line in input.splitlines():
        w_nums, nums = line.split("|")
        c_num, w_nums = w_nums.split(":")
        c_num = int(c_num.split()[1])
        w_nums = list(map(int, w_nums.split()))
        nums = list(map(int, nums.split()))
        cards.append([len(set(w_nums) & set(nums))])
    for i, card in enumerate(cards):

        for c in card:
            if c > 0:
                for j in range(i + 1, i + c + 1):
                    cards[j].append(cards[j][0])
    return len([y for x in cards for y in x])


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
