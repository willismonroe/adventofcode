import pathlib
from collections import deque

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

example_input2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

corners = str.maketrans(
    {"L": "└", "J": "┘", "7": "┐", "F": "┌", "-": "─", "|": "│", ".": " "}
)


def parse_input(inp):
    start: tuple = ()
    inp = inp.translate(corners)
    for y, line in enumerate(inp.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                start = (y, x)
    map_array = [[c for c in line] for line in inp.splitlines()]
    return map_array, start


def part1(input):
    # input = example_input2
    map_array, start = parse_input(input)
    map_array[start[0]][start[1]] = "┌"
    max_y, max_x = (len(map_array), len(map_array[0]))
    distance_array = [["." for x in range(max_x)] for y in range(max_y)]
    for line in distance_array:
        print("".join(map(str, line)))
    queue = deque([(start, 0)])
    seen = set()
    max_distance = 0
    while queue:
        node, distance = queue.popleft()
        y, x = node
        # print(y, x, map_array[y][x], distance)
        distance_array[y][x] = distance
        for line in distance_array:
            print("".join(map(str, line)))
        print()
        if node in seen:
            continue
        seen.add(node)
        if node == start and distance > 0:
            print(distance)
            max_distance = distance
            break
        match map_array[y][x]:
            case "└":
                if y > 0:
                    new_node = (y - 1, x)
                    if new_node not in seen:
                        queue.append(((y - 1, x), distance + 1))
                if x < max_x:
                    new_node = (y, x + 1)
                    if new_node not in seen:
                        queue.append(((y, x + 1), distance + 1))
            case "┘":
                if y > 0:
                    new_node = (y - 1, x)
                    if new_node not in seen:
                        queue.append(((y - 1, x), distance + 1))
                if x > 0:
                    new_node = (y, x - 1)
                    if new_node not in seen:
                        queue.append(((y, x - 1), distance + 1))
            case "┐":
                if y < max_y:
                    new_node = (y + 1, x)
                    if new_node not in seen:
                        queue.append(((y + 1, x), distance + 1))
                if x > 0:
                    new_node = (y, x - 1)
                    if new_node not in seen:
                        queue.append(((y, x - 1), distance + 1))
            case "┌":
                if y < max_y:
                    new_node = (y + 1, x)
                    if new_node not in seen:
                        queue.append(((y + 1, x), distance + 1))
                if x < max_x:
                    new_node = (y, x + 1)
                    if new_node not in seen:
                        queue.append(((y, x + 1), distance + 1))
            case "─":
                if x > 0:
                    new_node = (y, x - 1)
                    if new_node not in seen:
                        queue.append(((y, x - 1), distance + 1))
                if x < max_x:
                    new_node = (y, x + 1)
                    if new_node not in seen:
                        queue.append(((y, x + 1), distance + 1))
            case "│":
                if y > 0:
                    new_node = (y - 1, x)
                    if new_node not in seen:
                        queue.append(((y - 1, x), distance + 1))
                if y < max_y:
                    new_node = (y + 1, x)
                    if new_node not in seen:
                        queue.append(((y + 1, x), distance + 1))
    print(distance)
    return distance


def part2(input):
    return 0


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
