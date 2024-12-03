import pathlib
from json import loads
from functools import cmp_to_key

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

def parse_input(inp, pairs=True):
    if pairs:
        lines = [[loads(line) for line in pair.splitlines()] for pair in inp.split('\n\n')]
    else:
        lines = [loads(line) for line in inp.splitlines() if line != '']
    return lines

def compare(a, b):
    a_is_int = type(a) is int
    b_is_int = type(b) is int

    if a_is_int and b_is_int:
        return a - b

    if a_is_int != b_is_int:
        if a_is_int:
            return compare([a], b)
        else:
            return compare(a, [b])
    
    for x, y in zip(a, b):
        res = compare(x, y)
        if res != 0:
            return res

    return len(a) - len(b)


def part1(input):
    pairs = parse_input(input)
    ordered = []
    for i, pair in enumerate(pairs, 1):
        if compare(pair[0], pair[1]) < 0:
            ordered.append(i)
    return sum(ordered)


def part2(input):
    lines = parse_input(input, pairs=False)
    lines.extend(([[2]], [[6]]))
    lines.sort(key=cmp_to_key(compare))
    answer = lines.index([[2]]) + 1
    answer *= lines.index([[6]]) + 1
    return answer


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
