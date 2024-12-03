import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


example_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

CYCLES = {"addx": 2, "noop": 1}


def parse_input(inp):
    ops = []
    for line in inp.splitlines():
        line = line.split()
        if len(line) > 1:
            ops.append([line[0], int(line[1])])
        else:
            ops.append([line[0]])
    return ops


def part1(input):
    ops = parse_input(input)
    cycle = 1
    signal_strength_values = 0
    X = 1
    for op in ops:
        cycle += 1
        match op[0]:
            case "noop":
                pass
            case "addx":
                if cycle % 40 == 20:
                    signal_strength_values += cycle * X
                cycle += 1
                X += op[1]

        if cycle % 40 == 20:
            signal_strength_values += cycle * X

    return signal_strength_values


def part2(input):
    ops = parse_input(input)
    cycle = 1
    crt = []
    row = ""
    X = 1
    for op in ops:
        row += '#' if X <= cycle % 40 < X + 3 else ' '

        cycle += 1

        match op[0]:
            case "noop":
                pass
            case "addx":
                if cycle % 40 == 1:
                    crt.append(row)
                    row = ""

                row += '#' if X <= cycle % 40 < X + 3 else ' '

                cycle += 1
                X += op[1]

        if cycle % 40 == 1:
            crt.append(row)
            row = ""

    return crt


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2:\n", '\n'.join(part2(input)), sep='')
