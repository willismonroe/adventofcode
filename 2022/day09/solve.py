import pathlib
import math

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

DELTA = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def sign(x):
    return (x > 0) - (x < 0)


def parse_input(inp):
    moves = []
    for line in inp.splitlines():
        dir, steps = line.split()
        steps = int(steps)
        moves.append((dir, steps))
    return moves


def part1(input):
    hx, hy = 0, 0
    tx, ty = 0, 0
    seen = {(0, 0)}
    moves = parse_input(input)

    for move in moves:
        dir, steps = move

        for _ in range(steps):
            deltax, deltay = DELTA[dir]
            hx += deltax
            hy += deltay
            dx = hx - tx
            dy = hy - ty

            if dx**2 + dy**2 > 2:
                if dx != 0:
                    tx += sign(dx)
                if dy != 0:
                    ty += sign(dy)

                seen.add((tx, ty))
    return len(seen)


def part2(input):
    rope = [(0, 0)] * 10
    seen_1 = {(0, 0)}
    seen_9 = {(0, 0)}
    moves = parse_input(input)

    for move in moves:
        dir, steps = move

        for _ in range(steps):
            hx, hy = rope[0]
            dx, dy = DELTA[dir]
            rope[0] = hx + dx, hy + dy

            for i in range(9):
                hx, hy = rope[i]
                tx, ty = rope[i + 1]
                dx, dy = hx - tx, hy - ty

                if dx**2 + dy**2 > 2:
                    rope[i + 1] = tx + sign(dx), ty + sign(dy)

            seen_1.add(tuple(rope[1]))
            seen_9.add(tuple(rope[9]))

    return len(seen_9)


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
