import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse_input(inp):
    inp = inp.splitlines()
    for i, line in enumerate(inp):
        if line == '':
            return parse_stacks(inp[:i-1]), parse_inst(inp[i+1:])

def parse_stacks(inp):
    stacks = [[] for _ in range(len(inp[0]) // 4 + 1)]
    for line in inp:
        for i, stack in enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
            if stack.strip() != '':
                stacks[i].append(stack.strip().replace('[', '').replace(']',''))
    stacks = [stack[::-1] for stack in stacks]
    return stacks

def parse_inst(inp):
    insts = []
    for line in inp:
        _, num, _, start, _, end = line.split()
        insts.append([int(num), int(start)-1, int(end)-1])
    return insts

def part1(input):
    stacks, insts = parse_input(input)
    crane = []
    for inst in insts:
        num, start, end = inst
        for i in range(num):
            crane.append(stacks[start].pop())
            stacks[end].append(crane.pop())
    return "".join([stack[-1] for stack in stacks])


def part2(input):
    stacks, insts = parse_input(input)
    crane = []
    for inst in insts:
        num, start, end = inst
        for i in range(num):
            crane.append(stacks[start].pop())
        for i in range(num):
            stacks[end].append(crane.pop())
    return "".join([stack[-1] for stack in stacks])

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = test_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
