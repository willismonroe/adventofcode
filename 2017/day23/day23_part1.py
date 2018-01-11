import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day23_input.txt").read().splitlines()

    print(solve(inp))


class Duet:
    def __init__(self, instructions):
        self.instructions = instructions
        self.cursor = 0
        self.registers = {i: 0 for i in ['a','b','c','d','e','f','g','h']}
        self.finished = 0
        self.mul_count = 0

    def grab(self, x):
        if x.isalpha():
            return self.registers[x]
        else:
            return int(x)

    def next(self):
        if self.cursor >= len(self.instructions):
            self.finished = 1
        else:
            ins, *p = self.instructions[self.cursor].split()
            if ins != 'jnz':
                if ins == 'set':
                    self.set(*p)
                elif ins == 'mul':
                    self.mul(*p)
                elif ins == 'sub':
                    self.sub(*p)
                self.cursor += 1
            elif ins == 'jnz':
                self.jnz(*p)
            else:
                print(f"Unknown instruction: {ins, *p}")

    def set(self, x, y):
        self.registers[x] = self.grab(y)

    def sub(self, x, y):
        self.registers[x] -= self.grab(y)

    def mul(self, x, y):
        self.mul_count += 1
        self.registers[x] *= self.grab(y)

    def jnz(self, x, y):
        if self.grab(x) != 0:
            self.cursor += self.grab(y)
        else:
            self.cursor += 1


def solve(inp):
    d = Duet(inp)
    while d.finished == 0:
        d.next()

    return d.mul_count


if __name__ == '__main__':
    main()
