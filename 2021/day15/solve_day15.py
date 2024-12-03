import heapq
from collections import defaultdict
from math import inf as INFINITY


def main():
    raw_input = open('day15_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < w and 0 <= cc < h:
            yield rr, cc


def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    source = (0, 0)
    destination = (h - 1, w - 1)

    queue = [(0, source)]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    visited = set()

    while queue:
        dist, node = heapq.heappop(queue)

        if node == destination:
            return dist

        if node in visited:
            continue

        visited.add(node)
        r, c = node

        for neighbor in neighbors4(r, c, h, w):
            if neighbor in visited:
                continue
            
            nr, nc = neighbor
            newdist = dist + grid[nr][nc]

            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))
    return INFINITY


def part1(raw_input):
    lines = map(str.rstrip, raw_input.splitlines())
    grid = list(list(map(int, row)) for row in lines)
    return dijkstra(grid) 

def part2(raw_input):
    lines = map(str.rstrip, raw_input.splitlines())
    grid = list(list(map(int, row)) for row in lines)
    tilew = len(grid)
    tileh = len(grid[0])

    for _ in range(4):
        for row in grid:
            tail = row[-tilew:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(4):
        for row in grid[-tileh:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)

    return dijkstra(grid)



if __name__ == "__main__":
    main()
