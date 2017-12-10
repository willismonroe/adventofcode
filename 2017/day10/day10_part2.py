import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day10_input.txt").read()

    print(solve(input))


def solve(input, l=list(range(256))):
    input = list(map(ord, input)) + list(map(int, "17,31,73,47,23".split(',')))
    skip = 0
    pos = 0
    for _ in range(64):
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
    sparse_hash = [l[i:i + 16] for i in range(0, len(l), 16)]
    dense_hash = ''
    for hash in sparse_hash:
        h = hash[0]
        for i in hash[1:]:
            h = h ^ i
        h = hex(h)[2:]
        if len(h) == 1:
            dense_hash += '0' + h
        else:
            dense_hash += h

    return dense_hash


if __name__ == '__main__':
    main()
