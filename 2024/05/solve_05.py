import pathlib
from functools import cmp_to_key

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


# def check_valid(n: int, rule_dict: dict[int, list[int]]):
#     if


def parse_rules(rules: str):
    rules_dict: dict[int, list[int]] = {}
    for rule in rules.splitlines():
        b, a = map(int, rule.split("|"))
        if a in rules_dict:
            rules_dict[a].append(b)
        else:
            rules_dict[a] = [b]
        if b not in rules_dict:
            rules_dict[b] = []
    return rules_dict


def part1(puzzle_input: str) -> int:
    rules, updates = puzzle_input.split("\n\n")
    rules = parse_rules(rules)
    updates = [
        [int(num) for num in line.split(",")] for line in updates.splitlines()
    ]
    valid_updates: list[list[int]] = []
    for _, update in enumerate(updates):
        valid = True
        for i, num in enumerate(update[:-1]):
            if any(n in rules[num] for n in update[i:]):
                valid = False
        if valid:
            valid_updates.append(update)
    return sum(update[len(update) // 2] for update in valid_updates)


def part2(puzzle_input: str) -> int:
    rules, updates = puzzle_input.split("\n\n")
    rules = parse_rules(rules)
    updates = [
        [int(num) for num in line.split(",")] for line in updates.splitlines()
    ]
    invalid_updates: list[list[int]] = []
    for _, update in enumerate(updates):
        valid = True
        for i, num in enumerate(update[:-1]):
            if any(n in rules[num] for n in update[i:]):
                valid = False
        if not valid:
            invalid_updates.append(update)

    def cmp(x: int, y: int) -> int:
        return -1 if x in rules[y] else (0 if x == y else 1)

    total = 0
    for update in invalid_updates:
        total += sorted(update, key=cmp_to_key(cmp))[len(update) // 2]
    return total


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
