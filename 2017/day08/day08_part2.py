import os

import operator


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day08_input.txt").read().splitlines()

    print(solve(input))


operators = {
    ">": operator.gt,
    "<": operator.lt,
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    "<=": operator.le,
    "dec": operator.sub,
    "inc": operator.add
}


def solve(input):
    registers = {}
    highest = 0
    for line in input:
        register, instruction, number, \
        _, conditional_register, conditional_operator, compare_number = line.split()
        number, compare_number = map(int, [number, compare_number])
        if register not in registers.keys():
            registers[register] = 0
        if conditional_register not in registers.keys():
            registers[conditional_register] = 0

        if operators[conditional_operator](registers[conditional_register], compare_number):
            registers[register] = operators[instruction](registers[register], number)
            if registers[register] > highest:
                highest = registers[register]

    return highest


if __name__ == '__main__':
    main()
