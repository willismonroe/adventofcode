from collections import deque, defaultdict


def main():
    raw_input = open('day12_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

example_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example_input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def construct_graph(edges):
    graph = defaultdict(list)
    for orig, dest in [edge.split('-') for edge in edges]:
        if dest != 'start':
            graph[orig].append(dest)
        if orig != 'start':
            graph[dest].append(orig)
    return graph

def dfs_paths(graph, start, goal):
    stack = deque([(start, {start})])
    paths = 0

    while stack:
        node, visited = stack.pop()

        if node == goal:
            paths += 1
            continue

        for n in graph[node]:
            if n in visited and n.islower():
                continue

            stack.append((n, visited | {n}))

    return paths


def part1(raw_input):
    edges = raw_input.splitlines()
    graph = construct_graph(edges)
    paths = dfs_paths(graph, 'start', 'end')
    return paths


def dfs_paths2(graph, src, dst):
    stack = deque([(src, {src}, False)])
    paths = 0

    while stack:
        node, visited, double = stack.pop()
        if node == dst:
            paths += 1
            continue

        for n in graph[node]:
            if n not in visited or n.isupper():
                stack.append((n, visited | {n}, double))
                continue

            if double:
                continue

            stack.append((n, visited, True))

    return paths


def part2(raw_input):
    edges = raw_input.splitlines()
    graph = construct_graph(edges)
    paths = dfs_paths2(graph, 'start', 'end')
    return paths


if __name__ == "__main__":
    main()
