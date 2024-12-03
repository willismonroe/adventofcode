def main():
    raw_input = open('day09_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def part1(raw_input):
    hmap = [[int(n) for n in line] for line in raw_input.splitlines()]
    max_x = len(hmap[0])
    max_y = len(hmap)

    def neighbors(y, x):
        points = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        return [(a, b) for a, b in points if 0 <= a < max_y and 0 <= b < max_x]

    lowest = []
    for y in range(max_y):
        for x in range(max_x):
            if all(hmap[y][x] < hmap[a][b] for a, b in neighbors(y, x)):
                lowest.append(hmap[y][x] + 1)
    return sum(lowest)


def part2(raw_input):
    hmap = [[int(n) for n in line] for line in raw_input.splitlines()]
    max_x = len(hmap[0])
    max_y = len(hmap)

    def neighbors(y, x):
        points = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        return [(a, b) for a, b in points if 0 <= a < max_y and 0 <= b < max_x]

    lowpoints = []
    for y in range(max_y):
        for x in range(max_x):
            if all(hmap[y][x] < hmap[a][b] for a, b in neighbors(y, x)):
                lowpoints.append((y, x))

    def get_basin(y, x):
        # print("Checking y:", y, "x:", x, "cell:", hmap[y][x])
        basin = {(y, x)}
        for a, b in neighbors(y, x):
            # print("Found neighbor y:", a, "x:", b, "cell:", hmap[a][b])
            if hmap[y][x] < hmap[a][b] < 9:
                # print("Part of basin")
                basin |= get_basin(a, b)
        return basin

    basins = sorted([len(get_basin(y, x)) for y, x in lowpoints])
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":
    main()
