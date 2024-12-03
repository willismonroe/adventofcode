import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""


def part1(puzzle_input):
    list_a = sorted(
        [int(line.split("  ")[0]) for line in puzzle_input.splitlines()]
    )
    list_b = sorted(
        [int(line.split("  ")[1]) for line in puzzle_input.splitlines()]
    )
    dis = 0
    for a, b in zip(list_a, list_b):
        dis += abs(a - b)
    return dis


def part2(puzzle_input):
    list_a = sorted(
        [int(line.split("  ")[0]) for line in puzzle_input.splitlines()]
    )
    list_b = sorted(
        [int(line.split("  ")[1]) for line in puzzle_input.splitlines()]
    )
    sim_score = 0
    for num in list_a:
        sim_score += num * list_b.count(num)
    return sim_score


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        puzzle_input = f.read()
    # input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
