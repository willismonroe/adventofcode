import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


decode = {
    "A": 0,
    "X": 0,
    "B": 1,
    "Y": 1,
    "C": 2,
    "Z": 2,
}


def parse_input(input):
    rounds = input.splitlines()
    pairs = []
    for round in rounds:
        p1, p2 = round.split()
        pairs.append((decode[p1], decode[p2]))
    return pairs


def play_round(p1, p2):
    if p1 == p2:
        return 3 + p2 + 1
    if (p1 + p2) % 2:  # same parity
        if max(p1, p2) == p2:
            return 6 + p2 + 1
        else:
            return 0 + p2 + 1
    else:
        if min(p1, p2) == p2:
            return 6 + p2 + 1
        else:
            return 0 + p2 + 1


def part1(input):
    pairs = parse_input(input)
    score = 0
    for p1, p2 in pairs:
        score += play_round(p1, p2)
    return score


def part2(input):
    pairs = parse_input(input)
    score = 0
    for p1, p2 in pairs:
        if p2 == 0:  # lose
            for i in [0, 1, 2]:
                temp = play_round(p1, i)
                if temp == 0 + i + 1:
                    score += temp
        if p2 == 1:  # draw
            for i in [0, 1, 2]:
                temp = play_round(p1, i)
                if temp == 3 + i + 1:
                    score += temp
        if p2 == 2:  # win
            for i in [0, 1, 2]:
                temp = play_round(p1, i)
                if temp == 6 + i + 1:
                    score += temp
    return score


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
