def main():
    # solve for puzzle input
    input = open("day04_input.txt").read().splitlines()

    print(solve(input))


def solve(input):
    valid = 0
    for line in input:
        if len(set(line.split())) == len(line.split()):
            valid += 1

    return valid


if __name__ == "__main__":
    main()
