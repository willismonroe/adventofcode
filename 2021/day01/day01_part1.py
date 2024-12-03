def main():
    puzzle_input = open('part1_input.txt').read()

    print(solve(puzzle_input))

def solve(puzzle_input):
    m = puzzle_input.splitlines()
    inc = 0
    prev = m[0]
    for n in m[1:]:
        if int(n) > int(prev):
            inc += 1
        prev = n
    return inc

if __name__ == "__main__":
    main()