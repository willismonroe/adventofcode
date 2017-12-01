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

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __cmp__(self, other):
        return self.x, self.y == other.x, other.y

def solve(data):
    nodes = []
    for line in data:
        nodes.append(Node(line))

    valid_nodes = 0
    for outer_node in nodes:
        for inner_node in nodes:
            if outer_node == inner_node:
                continue
            if outer_node.used == 0:
                continue
            if outer_node.used < inner_node.avail:
                valid_nodes += 1
    return valid_nodes

def solve_v2(data):
    nodes = []
    for line in data:
        nodes.append(Node(line))

    grid = [[[] for i in range(35)] for i in range(30)]
    for node in nodes:
        icon = '.'
        if node.used == 0:
            icon = "_"
        if node.size > 400:
            icon = "#"
        if node.x == 29 and node.y == 0:
            icon = "G"
        grid[node.x][node.y] = icon

    with open('output.txt', 'w') as f:
        for row in grid:
            f.write(','.join(row) + '\n')


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()[2:]

    print(solve(data))

    print(solve_v2(data))