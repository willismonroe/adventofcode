import pathlib
import re

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example_input2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

example_input3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def part1(input):
    # input = example_input2
    ins, nodes = input.split("\n\n")
    ins = ins.replace("L", "0").replace("R", "1")
    nodes = {
        line.split("=")[0].strip(): re.findall("\w{3}", line.split("=")[1])
        for line in nodes.splitlines()
    }
    # print(ins, nodes)
    c = 0
    moves = 0
    node = 'AAA'
    while node != 'ZZZ':
        instruction = ins[c % len(ins)]
        # print(node, instruction, nodes[node])
        node = nodes[node][int(instruction)]
        c += 1
        moves += 1

    return moves


def part2(input):
    return 0


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
