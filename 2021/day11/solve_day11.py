from itertools import product


def main():
    raw_input = open('day11_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def get_neighbors(x, y, max_x, max_y):
    return [(a, b) for a, b in product(range(x - 1, x + 2), range(y - 1, y + 2))
            if (a, b) != (x, y) and 0 <= a < max_x and 0 <= b < max_y]


def print_board(graph):
    for row in graph:
        line = ''
        for cell in row:
            line += str(cell)
        print(line)


def part1(raw_input):
    # raw_input = example_input
    graph = [[int(cell) for cell in line] for line in raw_input.splitlines()]
    flashes = 0
    max_x = len(graph[0])
    max_y = len(graph)
    for step in range(100):
        flashed = []

        def flash(x, y):
            flashed.append((x, y))
            graph[y][x] = 0
            for a, b in get_neighbors(x, y, max_x, max_y):
                if (a, b) not in flashed:
                    graph[b][a] += 1
                    if graph[b][a] > 9:
                        flash(a, b)

        for x, y in product(range(max_x), range(max_y)):
            if (x, y) not in flashed:
                graph[y][x] += 1
                if graph[y][x] > 9:
                    flash(x, y)

        # print("\nEnd of step:", step+1)
        # print_board(graph)
        flashes += len(flashed)

    return flashes


def part2(raw_input):
    # raw_input = example_input
    graph = [[int(cell) for cell in line] for line in raw_input.splitlines()]
    flashes = 0
    max_x = len(graph[0])
    max_y = len(graph)
    step = 0
    done = False
    while not done:
        flashed = []

        def flash(x, y):
            flashed.append((x, y))
            graph[y][x] = 0
            for a, b in get_neighbors(x, y, max_x, max_y):
                if (a, b) not in flashed:
                    graph[b][a] += 1
                    if graph[b][a] > 9:
                        flash(a, b)

        for x, y in product(range(max_x), range(max_y)):
            if (x, y) not in flashed:
                graph[y][x] += 1
                if graph[y][x] > 9:
                    flash(x, y)

        if all(y == 0 for x in graph for y in x):
            done = True
        else:
            step += 1
    return step + 1


if __name__ == "__main__":
    main()
