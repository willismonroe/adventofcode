import os

from collections import deque


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = int(open("day17_input.txt").read())

    print(solve(input))


def solve(input):
    buffer = deque([0])
    for i in range(1, 50_000_000 + 1):
        buffer.rotate(-input)
        buffer.append(i)

    return buffer[buffer.index(0) + 1]


if __name__ == '__main__':
    main()
