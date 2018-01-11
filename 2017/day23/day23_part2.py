import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day23_input.txt").read().splitlines()

    print(solve(inp))


def solve(inp):
    h, g = 0, 0
    c = 122700
    for b in range(105700, c + 1, 17):
        if any(b % d == 0 for d in range(2, int(b**0.5))):
            h += 1
    return h


if __name__ == '__main__':
    main()
