def main():
    # solve for puzzle input
    input = list(map(int, open("day05_input.txt").read().splitlines()))

    print(solve(input))


def solve(input):
    count = 0
    index = 0

    # 0 3 0 1 -3
    while 1:
        try:
            jump = input[index]
            old_index = index
            index = index + jump
            input[old_index] += 1
            count += 1
        except IndexError:
            break

    return count


if __name__ == "__main__":
    main()
