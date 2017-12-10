import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day10_input.txt").read()

    print(solve(input))


def solve(input, l=list(range(256))):
    input = list(map(ord, input)) + list(map(int, "17,31,73,47,23".split(',')))
    skip = 0
    pos = 0
    inc = lambda x, d: (x + d) % len(l)
    for _ in range(64):
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
    sparse_hash = [l[i:i + 16] for i in range(0, len(l), 16)]
    dense_hash = ''
    for hash in sparse_hash:
        h = hash[0]
        for i in hash[1:]:
            h = h ^ i
        dense_hash += f'{h:02x}'

    return dense_hash


if __name__ == '__main__':
    main()
