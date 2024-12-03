from collections import Counter, defaultdict


def main():
    raw_input = open('day14_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

def react(poly, rules, n, last):
    for _ in range(n):
        newpoly = defaultdict(int)

        for pair in poly:
            products = rules.get(pair)

            if products:
                n = poly[pair]
                newpoly[products[0]] += n
                newpoly[products[1]] += n
            else:
                newpoly[pair] = poly[pair]

        poly = newpoly
    counts = defaultdict(int, {last: 1})
    for (a, _), n in poly.items():
        counts[a] += n

    return poly, max(counts.values()) - min(counts.values())


def part1(raw_input):
    lines = raw_input.splitlines()
    template = [c for c in lines[0]]
    rules = [line.split(' -> ') for line in lines[2:]]
    for step in range(10):
        new_template = []
        for i in range(1, len(template)):
            for rule in rules:
                if rule[0][0] == template[i-1] and rule[0][1] == template[i]:
                    new_template.extend([template[i-1], rule[1]])
        new_template.append(template[i])
        template = new_template

    c = Counter(template)
    return c.most_common()[0][1] - c.most_common()[-1][1]


def part2(raw_input):
    template = [c for c in raw_input.splitlines()[0]]
    rules = {}
    for line in map(str.rstrip, raw_input.splitlines()[2:]):
        (a, b), c = line.split(' -> ')
        rules[a, b] = ((a, c), (c, b))

    poly = Counter(zip(template, template[1:]))
    poly, answer1 = react(poly, rules, 10, template[-1])
    poly, answer2 = react(poly, rules, 30, template[-1])

    return answer2




if __name__ == "__main__":
    main()
