import pathlib
from operator import add, mul, attrgetter
from math import lcm
from collections import deque

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class Monkey:
    def __init__(self, id, starting, op, test, true, false) -> None:
        self.id = id
        self.items = deque(starting)
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0

    def inspect(self):
        item = self.items.popleft()

        if self.op["value"] is None:
            return self.op["op"](item, item)
        return self.op["op"](item, self.op["value"])


def parse_input(inp):
    monkeys = []
    for monkey in inp.split("\n\n"):
        id = 0
        starting = []
        op = {}
        test = 0
        true = 0
        false = 0
        for line in monkey.splitlines():
            match line.strip()[:4]:
                case "Monk":
                    id = int(line.split()[1][:-1])
                case "Star":
                    starting = list(map(int, line.split(":")[1].split(",")))
                case "Oper":
                    opr = "+" if "+" in line else "*"
                    op["op"] = add if "+" in line else mul
                    op["value"] = (
                        None
                        if "old" in line.split("=")[1].split(opr)[1]
                        else int(line.split("=")[1].split(opr)[1])
                    )
                case "Test":
                    test = int(line.split("by")[1])
                case "If t":
                    true = int(line.split("monkey")[1])
                case "If f":
                    false = int(line.split("monkey")[1])

        monkeys.append(Monkey(id, starting, op, test, true, false))
    return monkeys


def part1(input):
    monkeys = parse_input(input)
    for i in range(20):
        for m in monkeys:
            m.inspections += len(m.items)

            while m.items:
                item = m.inspect() // 3

                if item % m.test == 0:
                    monkeys[m.true].items.append(item)
                else:
                    monkeys[m.false].items.append(item)

    a, b = sorted(map(attrgetter("inspections"), monkeys), reverse=True)[:2]

    return a * b


def part2(input):
    monkeys = parse_input(input)
    modulus = lcm(*map(attrgetter('test'), monkeys))
    for i in range(10000):
        for m in monkeys:
            m.inspections += len(m.items)

            while m.items:
                item = m.inspect() % modulus

                if item % m.test == 0:
                    monkeys[m.true].items.append(item)
                else:
                    monkeys[m.false].items.append(item)

    a, b = sorted(map(attrgetter("inspections"), monkeys), reverse=True)[:2]

    return a * b


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
