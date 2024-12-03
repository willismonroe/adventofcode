from statistics import median, mean
from math import floor, ceil


def main():
    raw_input = open('input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = "16,1,2,0,4,2,7,1,2,14"


def part1(raw_input):
    nums = [int(n) for n in raw_input.split(',')]
    mp = floor(median(nums))
    fuel = 0
    for n in nums:
        fuel += abs(n - mp)
    return fuel


def part2(raw_input):
    nums = [int(n) for n in raw_input.split(',')]
    mp = ceil(mean(nums))
    fuel = []
    for i, m in enumerate(range(mp - 1, mp + 2)):
        fuel.append(0)
        for n in nums:
            fuel[i] += abs(n - m) * (abs(n - m) + 1) // 2
    return min(fuel)


if __name__ == "__main__":
    main()
