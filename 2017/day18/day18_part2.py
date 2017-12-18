import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day18_input.txt").read().splitlines()

    print(solve(input))


class Duet:
    def __init__(self, instructions, id):
        self.instructions = instructions
        self.id = id
        self.cursor = 0
        self.registers = {i: 0 for i in [x.split()[1] for x in self.instructions] if i.isalpha()}
        self.registers['p'] = self.id
        self.sound = 0
        self.r_sound = 0
        self.finished = 0
        self.queue = []
        self.send_count = 0
        self.waiting = 0
        self.partner = 0

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
        self.partner.queue.append(self.sound)
        self.send_count += 1

    def rcv(self, x):
        if self.queue:
            self.registers[x] = self.queue.pop(0)
        else:
            self.cursor -= 1
            self.waiting = 1

    def set(self, x, y):
        self.registers[x] = self.grab(y)

    def add(self, x, y):
        self.registers[x] += self.grab(y)

    def mul(self, x, y):
        self.registers[x] *= self.grab(y)

    def mod(self, x, y):
        self.registers[x] = self.registers[x] % self.grab(y)

    def jgz(self, x, y):
        if self.grab(x) > 0:
            self.cursor += self.grab(y)
        else:
            self.cursor += 1


def solve(input):
    zero = Duet(input, 0)
    one = Duet(input, 1)
    zero.partner = one
    one.partner = zero
    while sum([zero.waiting, one.waiting]) < 2:
        zero.next()
        one.next()

    return one.send_count


if __name__ == '__main__':
    main()
