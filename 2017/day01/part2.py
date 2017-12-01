def main():
    # solve for puzzle input
    input = open("part1_input.txt").read()

    print(solve(input))


def solve(captcha):
    sum = 0
    half = len(captcha) / 2
    for i, c in enumerate(captcha):
        if c == captcha[int((i + half) % len(captcha))]:
            sum += int(c)
    return sum


main()
