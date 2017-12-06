def main():
    # solve for puzzle input
    input = list(map(int, open("day06_input.txt").read().split('\t')))

    print(solve(input))


def solve(input):
    count = 0
    seen = []
    while input not in [t[0] for t in seen]:
        seen.append((input[:], count))
        # find highest
        index = input.index(max(input))
        value = input[index]
        input[index] = 0
        while value > 0:
            index = (index + 1) % len(input)
            input[index] += 1
            value -= 1
        count += 1

    return count - seen[[t[0] for t in seen].index(input)][1]


if __name__ == "__main__":
    main()
