import os, re


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
        for i, (v, a) in enumerate(zip(self.velocity, self.acceleration)):
            self.velocity[i] = v + a
        for i, (p, v) in enumerate(zip(self.position, self.velocity)):
            self.position[i] = p + v

    def distance(self):
        return sum(map(abs, self.position))


# p=<-4897,3080,2133>, v=<-58,-15,-78>, a=<17,-7,0>

PATTERN = "-?\d+"


def solve(input, cycles=1000):
    particles = []
    for line in input:
        m = re.findall(PATTERN, line)
        m = list(map(int, m))
        pos, vel, acc = m[:3], m[3:6], m[6:]
        particles.append(Particle(pos, vel, acc))

    count = 0
    while count < cycles:
        for p in particles:
            p.move()
        count += 1

    min_dist = min(particles, key=lambda p: p.distance())

    return particles.index(min_dist)


if __name__ == '__main__':
    main()
