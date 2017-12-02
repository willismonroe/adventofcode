from itertools import combinations

def main():
    # solve for puzzle input
    input = [[int(item) for item in line.strip('\n').split('\t')] for line in open("day02_input.txt").readlines()]
    print(solve(input))


def solve(input):
    checksum = 0
    for line in input:
        for pair in combinations(sorted(line, reverse=True), 2):
            if pair[0] % pair[1] == 0:
                checksum += pair[0] // pair[1]
    return checksum


main()
