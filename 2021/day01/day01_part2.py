def main():
    puzzle_input = open('part1_input.txt').read()

    print(solve(puzzle_input))

def solve(puzzle_input):
    m = [int(n) for n in puzzle_input.splitlines()]
    inc = 0
    prev = m[0] + m[1] + m[2]
    for i in range(len(m[:-2])):
        if m[i] + m[i+1] + m[i+2] > prev:
            inc += 1
        prev = m[i] + m[i+1] + m[i+2]
    return inc


if __name__ == "__main__":
    main()