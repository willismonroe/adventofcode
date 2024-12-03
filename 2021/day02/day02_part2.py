def main():
    puzzle_input = open('part1_input.txt').read()

    print(solve(puzzle_input))

def solve(puzzle_input):
    insts = puzzle_input.splitlines()
    h, d, a = 0, 0, 0
    for inst in insts:
        dir, n = inst.split()
        if dir[0] == 'f':
            h += int(n)
            d += (a * int(n))
        elif dir[0] == 'd':
            a += int(n)
        elif dir[0] == 'u':
            a -= int(n)
    return h * d


if __name__ == "__main__":
    main()