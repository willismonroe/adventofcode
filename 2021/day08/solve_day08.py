from typing import List


def main():
    raw_input = open('day08_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def part1(raw_input):
    output = [item.strip() for line in raw_input.splitlines()
              for item in line.split('|')[-1].split()]
    sum_digits = 0
    for char in output:
        if len(char) in [2, 4, 3, 7]:
            sum_digits += 1
    return sum_digits


def part2(raw_input):
    lines: list[list[list[str]]] = [[[''.join(sorted(word)) for word in side.split()] for side in line.split('|')] for
                                    line in raw_input.splitlines()]
    sum_digits = 0
    for wires, output in lines:
        connections: dict[int, str] = {}
        for item in sorted(wires, key=len):
            if len(item) == 2:
                connections[1] = item
            elif len(item) == 3:
                connections[7] = item
            elif len(item) == 4:
                connections[4] = item
            elif len(item) == 5:
                if set(connections[1]).issubset(item):
                    connections[3] = item
                elif len(set(item) - set(connections[4])) == 2:
                    connections[5] = item
                elif len(set(item) - set(connections[4])) == 3:
                    connections[2] = item
            elif len(item) == 6:
                if set(connections[5]).issubset(item):
                    if set(connections[4]).issubset(item):
                        connections[9] = item
                    elif not set(connections[4]).issubset(item):
                        connections[6] = item
                elif not set(connections[5]).issubset(item):
                    connections[0] = item
            elif len(item) == 7:
                connections[8] = item

        con_map = {v: k for k, v in connections.items()}
        num = ''
        for digit in output:
            num += str(con_map[digit])
        sum_digits += int(num)
    return sum_digits


if __name__ == "__main__":
    main()
