import os
from collections import defaultdict


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day24_input.txt").read().splitlines()

    print(solve(inp))

def generate_bridges(bridge, components):
    bridge = bridge or [(0,0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from generate_bridges(new, components)

def parse_components(inp):
    components = defaultdict(set)
    for l in inp:
        a, b = [int(x) for x in l.split('/')]
        components[a].add(b)
        components[b].add(a)
    return components

def solve(inp):
    components = parse_components(inp)
    bridges = []
    for bridge in generate_bridges(None, components):
        bridges.append((len(bridge), sum(a + b for a, b in bridge)))

    return sorted(bridges)[-1][1]


if __name__ == '__main__':
    main()
