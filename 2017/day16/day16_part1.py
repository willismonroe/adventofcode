import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day16_input.txt").read().split(',')

    print(solve(input))


def spin(programs, size):
    return programs[-size:] + programs[:-size]


def exchange(programs, a, b):
    p_list = programs[:]
    p_list[a], p_list[b] = p_list[b], p_list[a]
    return p_list


def partner(programs, a, b):
    return exchange(programs, programs.index(a), programs.index(b))


def solve(input):
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for move in input:
        if move[0] == 's':
            programs = spin(programs, int(move[1:]))
        elif move[0] == 'x':
            programs = exchange(programs, int(move[1:].split('/')[0]), int(move[1:].split('/')[1]))
        elif move[0] == 'p':
            programs = partner(programs, move[1:].split('/')[0], move[1:].split('/')[1])

    return ''.join(programs)


if __name__ == '__main__':
    main()
