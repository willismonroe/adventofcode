import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = list(map(int, open("day10_input.txt").read().split(',')))

    print(solve(input))


def solve(input, l=list(range(256))):
    skip = 0
    pos = 0
    inc = lambda x, d: (x + d) % len(l)
    for length in input:
        # reverse the slice
        indexes = [inc(pos, i) for i in range(length)]
        values = reversed([l[i] for i in indexes])
        for i, v in zip(indexes, values):
            l[i] = v
        # move forward
        pos += length + skip
        # increment skip
        skip += 1

    return l[0] * l[1]


if __name__ == '__main__':
    main()
