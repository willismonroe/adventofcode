# https://www.reddit.com/r/adventofcode/comments/7kz6ik/2017_day_20_solutions/dribj0c/
from collections import defaultdict

f = open("day20_input.txt", "r")


class Particle(object):
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def step(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def dist(self):
        return sum([abs(x) for x in self.p])


parts = {}
i = 0
for line in f:
    ts = line.strip().split(", ")
    ps = [int(x) for x in ts[0].split("=")[1][1:-1].split(",")]
    vs = [int(x) for x in ts[1].split("=")[1][1:-1].split(",")]
    acs = [int(x) for x in ts[2].split("=")[1][1:-1].split(",")]
    parts[i] = Particle(ps, vs, acs)
    i += 1

part2 = True
count = 0
cycles = 39
while count < cycles:
    min_d = None
    min_part = None
    for i, part in parts.items():
        part.step()
        if min_d is None or part.dist() < min_d:
            min_part = i
            min_d = part.dist()

    if part2:
        pos_dict = defaultdict(list)
        for i, part in parts.items():
            k = tuple(part.p)
            pos_dict[k].append(i)

        for k, v in pos_dict.items():
            if len(v) > 1:
                for i in v:
                    del parts[i]

        print(count, len(parts))
    else:
        print(min_part)
    count += 1
