import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day14_input.txt").read()

    print(solve(input))


def knot_hash(input, l=list(range(256))):
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


def hash_to_binary(hash):
    output = ''
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for c in hash:
        output += '{0:04b}'.format(hex.index(c))

    return output

def create_grid(input):
    grid = []
    for row in range(128):
        key = f'{input}-{row}'
        hash = knot_hash(key, l=list(range(256)))
        binary = hash_to_binary(hash)
        line = []
        for c in binary:
            line.append('#' if c == '1' else '.')
        grid.append(line)

    return grid

def solve(input):
    grid = create_grid(input)
    return sum(line.count('#') for line in grid)


if __name__ == '__main__':
    main()
