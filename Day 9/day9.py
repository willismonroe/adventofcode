import re

REGEX = re.compile("\((\d+x\d+)\)")

new_string = ''
def decompress(string):
    global new_string
    for m in REGEX.finditer(string):
        slice, times = map(int, m.group(1).split('x'))
        start, end = m.start(), m.end()
        slice = string[end:end+slice]
        print("{} means repeat \"{}\" {} times".format(m.group(1), slice, times))
        new_string += slice * times


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    print(len(decompress(data)))