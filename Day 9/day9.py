import re

REGEX = re.compile("\((\d+x\d+)\)")


def decompress(string):
    for m in REGEX.finditer(string):
        slice, times = map(int, m.group(1).split('x'))
        start, end = m.start(), m.end()
        print(string[start:end+5])

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    print(len(decompress(data)))