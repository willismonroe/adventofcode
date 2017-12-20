import os, re

from itertools import combinations
from collections import defaultdict


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day20_input.txt").read().splitlines()

    print(solve(input))


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def move(self):
        for i in range(3):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]

    def distance(self):
        return sum(map(abs, self.position))


# p=<-4897,3080,2133>, v=<-58,-15,-78>, a=<17,-7,0>

PATTERN = "-?\d+"


def solve(input, cycles=39):
    particles = {}
    i = 0
    for line in input:
        m = re.findall(PATTERN, line)
        m = list(map(int, m))
        pos, vel, acc = m[:3], m[3:6], m[6:]
        particles[i] = Particle(pos, vel, acc)
        i += 1

    count = 0
    while count < cycles:
        for i, p in particles.items():
            p.move()

        positions = defaultdict(list)
        for i, p in particles.items():
            k = tuple(p.position)
            positions[k].append(i)

        for k, v in positions.items():
            if len(v) > 1:
                for i in v:
                    del particles[i]

        count += 1

    return len(particles)


if __name__ == '__main__':
    main()
