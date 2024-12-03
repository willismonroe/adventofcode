import pathlib
from itertools import product

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """30373
25512
65332
33549
35390"""


def parse_input(inp):
    return [[int(c) for c in line] for line in inp.splitlines()]


def part1(input):
    trees = parse_input(input)
    num_trees = len(trees) * 2 + len(trees[0]) * 2 - 4
    interior = product(range(1, len(trees) - 1), repeat=2)
    for x, y in interior:
        tree = trees[x][y]
        column = [row[y] for row in trees]
        # check row:
        # print(x, y)
        # print(tree)
        # print(trees[x][:y], tree, trees[x][y + 1 :])
        # print(column[:x], tree, column[x + 1 :])
        if (
            tree > max(trees[x][:y])
            or tree > max(trees[x][y + 1 :])
            or tree > max(column[:x])
            or tree > max(column[x + 1 :])
        ):
            # print("***")
            num_trees += 1
        # print(num_trees)
        # print()
    return num_trees


def part2(input):
    trees = parse_input(input)
    scenic_scores = []
    interior = product(range(1, len(trees) - 1), repeat=2)
    # interior = [(1, 2)]
    for x, y in interior:
        # print()
        tree = trees[x][y]
        row = trees[x]
        column = [row[y] for row in trees]
        left = trees[x][:y][::-1]
        right = trees[x][y + 1 :]
        up = column[:x][::-1]
        down = column[x + 1 :]
        # print(left[::-1], tree, right)
        # print(up[::-1], tree, down)
        left_score = 0
        for i, ot in enumerate(left, 1):
            left_score += 1
            # print(f"tree: {tree}, i: {i}, value: {ot}, left_score: {left_score}")
            if ot >= tree:
                break
        right_score = 0
        for i, ot in enumerate(right, 1):
            right_score += 1
            # print(f"tree: {tree}, i: {i}, value: {ot}, right_score: {right_score}")
            if ot >= tree:
                break
        up_score = 0
        for i, ot in enumerate(up, 1):
            up_score += 1
            # print(f"tree: {tree}, i: {i}, value: {ot}, up_score: {up_score}")
            if ot >= tree:
                break
        down_score = 0
        for i, ot in enumerate(down, 1):
            down_score += 1
            # print(f"tree: {tree}, i: {i}, value: {ot}, down_score: {down_score}")
            if ot >= tree:
                break
        score = left_score * right_score * up_score * down_score
        scenic_scores.append(score)
    return max(scenic_scores)


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
