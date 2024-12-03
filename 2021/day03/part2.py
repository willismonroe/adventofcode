from collections import Counter 

def main():
    puzzle_input = open('part1_input.txt').read()

    print(solve(puzzle_input))


def solve(puzzle_input):
    lines = puzzle_input.splitlines()
    l = len(lines[0])
    for i in range(l):
        mcs = Counter([int(line[i]) for line in lines]).most_common()
        if len(mcs) > 1 and mcs[0][1] == mcs[1][1]:
            mc = 1
        else:
            mc = Counter([int(line[i]) for line in lines]).most_common(1)[0][0]
        lines = [line for line in lines if int(line[i]) == mc]
        print(lines)
    ox_gen = int(lines[0], 2)
    print(ox_gen)

    lines = puzzle_input.splitlines()
    for i in range(l):
        mcs = Counter([int(line[i]) for line in lines]).most_common()
        if len(mcs) > 1 and mcs[0][1] == mcs[1][1]:
            lc = 0
        else:
            lc = Counter([int(line[i]) for line in lines]).most_common()[-1][0]
        lines = [line for line in lines if int(line[i]) == lc]
    co_scrub = int(lines[0], 2)
    print(co_scrub)
    return ox_gen * co_scrub

if __name__ == "__main__":
    main()
