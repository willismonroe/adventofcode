from itertools import permutations


def main():
    # solve for puzzle input

    input = open("day04_input.txt").read().splitlines()

    print(solve(input))


def solve(input):
    count = 0
    for line in input:
        # perms = [''.join(p) for word in line.split() for p in set(permutations(word))]
        perms = [''.join(sorted(word)) for word in line.split()]
        if len(perms) == len(set(perms)):
            count += 1
    return count


if __name__ == "__main__":
    main()
