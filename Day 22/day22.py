import re

REGEX = re.compile(r'x(?P<x>\d{1,2})-y(?P<y>\d{1,2})\s+(?P<size>\d{1,3})T\s+(?P<used>\d{1,3})T\s+(?P<avail>\d{1,3})T\s+(?P<use>\d{1,2})')

class Node:
    def __init__(self, line):
        line = list(REGEX.finditer(line))[0].groupdict()
        line = {key:int(line[key]) for key in line.keys()}
        self.x = line['x']
        self.y = line['y']
        self.size = line['size']
        self.used = line['used']
        self.avail = line['avail']
        self.use = line['use']


def solve(data):
    nodes = []
    for line in data:
        nodes.append(Node(line))



    print(nodes)

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()[2:]

    print(solve(data))