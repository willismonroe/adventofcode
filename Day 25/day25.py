from collections import OrderedDict

class Assembunny:
    def __init__(self, program, registers, limit=0):
        self.registers = registers
        self.program = program
        self.cursor = 0
        self.end = 0
        self.count = 0
        self.limit = limit

    def cpy(self, x, y):
        if x not in self.registers.keys():
            self.registers[y] = int(x)
        else:
            self.registers[y] = self.registers[x]
        self.cursor += 1

    def inc(self, x):
        self.registers[x] += 1
        self.cursor += 1

    def dec(self, x):
        self.registers[x] -= 1
        self.cursor += 1

    def jnz(self, x, y):
        if (x, y) == ('0', '0'):
            # NOOP
            self.cursor += 1
        else:
            if x not in self.registers.keys() and int(x) != 0:
                if y not in self.registers.keys():
                    y = int(y)
                else:
                    y = int(self.registers[y])
                self.cursor += y
            elif self.registers[x] != 0:
                self.cursor += int(y)
            else:
                self.cursor += 1

    def tgl(self, x):
        try:
            if x not in self.registers.keys():
                x = int(x)
            else:
                x = int(self.registers[x])
            target_index = self.cursor + x
            target = self.program[target_index]
            if target[0] == 'inc':
                self.program[target_index] = ['dec', target[1]]
            elif target[0] == 'dec' or target[0] == 'tgl':
                self.program[target_index] = ['inc', target[1]]
            elif target[0] == 'jnz':
                self.program[target_index] = ['cpy', target[1], target[2]]
            elif target[0] == 'cpy':
                self.program[target_index] = ['jnz', target[1], target[2]]
        except:
            # out of bounds
            pass
        self.cursor += 1

    # Added an out command
    def out(self, x):
        if x in self.registers.keys():
            value = self.registers[x]
        else:
            value = int(x)
        print("OUT: {}".format(value))
        self.cursor += 1

    def run_line(self):
        try:
            line = self.program[self.cursor]
            #self.print_state()
            if line[0] == 'cpy':
                self.cpy(line[1], line[2])
            elif line[0] == 'inc':
                self.inc(line[1])
            elif line[0] == 'dec':
                self.dec(line[1])
            elif line[0] == 'jnz':
                self.jnz(line[1], line[2])
            elif line[0] == 'out':
                self.out(line[1])
            elif line[0] == 'tgl':
                self.tgl(line[1])
            self.count += 1
            if self.count == self.limit:
                self.end = 1
        except IndexError:
            self.end = 1

    def print_state(self):
        print("REGS: {}.".format(' '.join(['{}: {} '.format(key, value) for key, value in sorted(self.registers.items())])))
        print("LINE: {}.".format(' '.join(self.program[self.cursor])))


def solve(data, registers={'a': 158, 'b': 0, 'c': 0, 'd': 0, 'e': 0}):
    data = [line.split() for line in data]
    computer = Assembunny(data, registers)
    while computer.end == 0:
        computer.run_line()
    return computer.registers['a']

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    print(solve(data))