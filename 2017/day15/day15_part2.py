import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day15_input.txt").read().splitlines()

    print(solve(input))


class Generator:
    def __init__(self, starting_value, factor, multiple=1):
        self.previous_value = starting_value
        self.factor = factor
        self.multiple = multiple

    def generate(self):
        self.previous_value = (self.previous_value * self.factor) % 2147483647
        if self.previous_value % self.multiple == 0:
            return self.previous_value
        else:
            return self.generate()


def to_binary(value):
    # 0xFFFF = '0b1111111111111111' if we do a bitwise '&'
    # that matches the first 16 bits of the value thus selecting
    # them.
    return value & 0xFFFF


def solve(input):
    gen_a = Generator(int(input[0].split()[-1]), 16807, 4)
    gen_b = Generator(int(input[1].split()[-1]), 48271, 8)
    matches = 0
    for i in range(5000000):
        if to_binary(gen_a.generate()) == to_binary(gen_b.generate()):
            matches += 1

    return matches


if __name__ == '__main__':
    main()
