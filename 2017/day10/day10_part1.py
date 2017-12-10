import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = list(map(int, open("day10_input.txt").read().split(',')))

    print(solve(input))


def solve(input, l=list(range(256))):
    skip = 0
    pos = 0
    for length in input:
        # reverse the slice
        to_reverse = []
        for i in range(length):
            cur = (pos + i) % len(l)
            to_reverse.append(l[cur])
        to_reverse.reverse()
        for i in range(length):
            cur = (pos + i) % len(l)
            l[cur] = to_reverse[i]
        # move forward
        pos = (pos + length + skip) % len(l)
        # increment skip
        skip += 1

    return l[0] * l[1]


if __name__ == '__main__':
    main()
