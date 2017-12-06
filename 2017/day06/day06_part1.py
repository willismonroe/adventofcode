def main():
    # solve for puzzle input
    input = list(map(int, open("day06_input.txt").read().split('\t')))

    print(solve(input))


def solve(input):
    count = 0
    seen = []
    while input not in seen:
        seen.append(input[:])
        # find highest
        index = input.index(max(input))
        value = input[index]
        input[index] = 0
        while value > 0:
            index = (index + 1) % len(input)
            input[index] += 1
            value -= 1
        count += 1

    return count


if __name__ == "__main__":
    main()
