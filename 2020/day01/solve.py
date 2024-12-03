from itertools import combinations

def main():
    raw_input = open('day01.txt').read()

    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


def part1(raw_input):
    num = []
    for line in raw_input.splitlines():
        num.append(int(line))

    for i in range(len(num)):
        chosen_number = num[i]
        for j in num[i+1:]:
            if chosen_number + j == 2020:
                return chosen_number * j


def part2(raw_input):
    num = []
    for line in raw_input.splitlines():
        num.append(int(line))

    for triple in combinations(num, 3):
        if sum(triple) == 2020:
            return triple[0] * triple[1] * triple[2]

if __name__ == "__main__":
    main()