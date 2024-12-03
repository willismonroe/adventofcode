import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def sign(a):
    if a == 0:
        return 0
    return 1 if a > 0 else -1


def parse_input(inp):
    grid = {}
    lines = [
        [
            list(map(lambda x: int(x), coord.strip().split(",")))
            for coord in line.split("->")
        ]
        for line in inp.splitlines()
    ]
    for line in lines:
        # print("parse_input:line", line)
        points = draw_line(line)
        # print("parse_input:points", points)
        for point in points:
            grid[point] = "#"
    return grid


def draw_line(coords):
    line = []
    for a, b in zip(coords[:-1], coords[1:]):
        # print("draw_lines:a,b", a, b)
        line.extend((tuple(a), tuple(b)))
        for point in get_points(a, b):
            # print("draw_lines:point", point)
            line.append(tuple(point))
    return line


def get_points(a, b):
    diff = [b[0] - a[0], b[1] - a[1]]
    step = [sign(x) for x in diff]
    dis = sum([abs(x) for x in diff]) - 1
    for i in range(dis):
        # print("get_points:", a[0] + step[0] * (i + 1), a[1] + step[1] * (i + 1))
        yield a[0] + step[0] * (i + 1), a[1] + step[1] * (i + 1)


def draw_grid(grid):
    max_x, min_x = max([point[0] for point in grid.keys()]), min(
        [point[0] for point in grid.keys()]
    )
    max_y, min_y = max([point[1] for point in grid.keys()]), 0
    for y in range(min_y, max_y+1):
        line = [y, ' ']
        for x in range(min_x, max_x+1):
            line.append(grid.get(tuple([x, y]), '.'))
        print(''.join([str(c) for c in line]))



def part1(input):
    grid = parse_input(input)
    max_y = max([point[1] for point in grid.keys()])
    not_abyss = True
    start = [500, 0]
    while not_abyss:
        sand = start
        moving = True
        while moving:
            # check abyss
            if sand[1] > max_y:
                not_abyss = False
                break
            # down
            if not grid.get((sand[0], sand[1]+1), None):
                sand = [sand[0], sand[1]+1]
            # diagonal left
            elif not grid.get((sand[0]-1, sand[1]+1), None):
                sand = [sand[0]-1, sand[1]+1]
            # diagonal right
            elif not grid.get((sand[0]+1, sand[1]+1), None):
                sand = [sand[0]+1, sand[1]+1]
            # can't move so stop in place
            else:
                moving = False
                grid[(sand[0], sand[1])] = 'o'
            # draw_grid(grid)
    return sum(value == 'o' for value in grid.values())


def part2(input):
    grid = parse_input(input)
    max_y = max([point[1] for point in grid.keys()])
    not_abyss = True
    start = [500, 0]
    while not_abyss:
        sand = start
        moving = True
        while moving:
            moved = False
            # check abyss
            if sand[1] > max_y:
                moving = False
                grid[(sand[0], sand[1])] = 'o'
                break
            # down
            if not grid.get((sand[0], sand[1]+1), None):
                sand = [sand[0], sand[1]+1]
                moved = True
            # diagonal left
            elif not grid.get((sand[0]-1, sand[1]+1), None):
                sand = [sand[0]-1, sand[1]+1]
                moved = True
            # diagonal right
            elif not grid.get((sand[0]+1, sand[1]+1), None):
                sand = [sand[0]+1, sand[1]+1]
                moved = True
            # can't move so stop in place
            else:
                moving = False
                grid[(sand[0], sand[1])] = 'o'
            
            if grid.get((500, 0)) == 'o':
                not_abyss = False
    # draw_grid(grid)
    return sum(value == 'o' for value in grid.values())


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
