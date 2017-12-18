import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day18_input.txt").read().splitlines()

    print(solve(input))


class Duet:
    def __init__(self, instructions):
        self.instructions = instructions
        self.cursor = 0
        self.registers = {i: 0 for i in [x.split()[1] for x in self.instructions] if i.isalpha()}
        self.sound = 0
        self.r_sound = 0
        self.finished = 0

    def grab(self, x):
        if x.isalpha():
            return self.registers[x]
        else:
            return int(x)

    def next(self):
        if self.cursor > len(self.instructions):
            print("Completed instruction set")
            self.finished = 1
        else:
            ins, *p = self.instructions[self.cursor].split()
            if ins != 'jgz':
                if ins == 'snd':
                    self.snd(*p)
                elif ins == 'set':
                    self.set(*p)
                elif ins == 'add':
                    self.add(*p)
                elif ins == 'mul':
                    self.mul(*p)
                elif ins == 'mod':
                    self.mod(*p)
                elif ins == 'rcv':
                    self.rcv(*p)
                self.cursor += 1
            elif ins == 'jgz':
                self.jgz(*p)
            else:
                print(f"Unknown instruction: {ins, *p}")

    def snd(self, x):
        self.sound = self.grab(x)

    def set(self, x, y):
        self.registers[x] = self.grab(y)

    def add(self, x, y):
        self.registers[x] += self.grab(y)

    def mul(self, x, y):
        self.registers[x] *= self.grab(y)

    def mod(self, x, y):
        self.registers[x] = self.registers[x] % self.grab(y)

    def rcv(self, x):
        if self.grab(x) != 0:
            self.r_sound = self.sound
        else:
            pass

    def jgz(self, x, y):
        if self.grab(x) > 0:
            self.cursor += self.grab(y)
        else:
            self.cursor += 1


def solve(input):
    d = Duet(input)
    while not d.r_sound:
        d.next()

    return d.r_sound


if __name__ == '__main__':
    main()
