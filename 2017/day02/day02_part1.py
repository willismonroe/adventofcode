def main():
    # solve for puzzle input
    input = [[int(item) for item in line.strip('\n').split('\t')] for line in open("day02_input.txt").readlines()]

    print(solve(input))


def solve(input):
    checksum = 0
    for line in input:
        checksum += max(line) - min(line)

    return checksum


main()
