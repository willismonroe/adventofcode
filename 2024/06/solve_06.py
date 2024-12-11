import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def parse_map(raw_map: str):
    return [[c for c in line] for line in raw_map.splitlines()]


# dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(puzzle_input: str) -> int:
    grid = parse_map(puzzle_input)
    gr, gc = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                gr, gc = r, c
    dir = 0
    visited: set[tuple[int, int]] = set()

    # def print_map():
    #     for r in range(len(grid)):
    #         line = ""
    #         for c in range(len(grid[r])):
    #             if (r, c) in visited:
    #                 line += "X"
    #             else:
    #                 line += grid[r][c]
    #         print(line)
    #     print()

    in_bounds = True
    while in_bounds:
        # print_map()
        # facing
        dr, dc = dirs[dir][0], dirs[dir][1]
        # check if we're looking out of bounds
        if (
            gr + dr > len(grid) - 1
            or gr + dr < 0
            or 0 > gc + dc
            or gc + dc > len(grid) - 1
        ):
            # mark current cell visited and break
            visited.add((gr, gc))
            in_bounds = False
            break
        else:
            # check if obstacle and turn
            forward = grid[gr + dr][gc + dc]
            if forward == "#":
                dir = (dir + 1) % 4
            else:
                visited.add((gr, gc))
                gr, gc = gr + dr, gc + dc

    return len(visited)


def part2(puzzle_input: str) -> int:
    return True


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
