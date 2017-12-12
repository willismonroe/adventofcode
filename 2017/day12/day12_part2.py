import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day12_input.txt").read().splitlines()

    print(solve(input))


villages = {}


def create_village(input):
    for line in input:
        village, pipes = line.split(' <-> ')
        pipes = pipes.split(', ')
        villages[village] = pipes


def count_pipes(village, seen):
    seen = []

    def linked_pipes(village):
        pipes = villages[village]
        for pipe in pipes:
            if pipe not in seen:
                seen.append(pipe)
                linked_pipes(pipe)

    linked_pipes(village)
    return seen


def solve(input):
    create_village(input)
    vs = list(villages.keys())
    groups = 0
    while vs:
        pipes = count_pipes(vs[0], seen=[])
        vs = [v for v in vs if v not in pipes]
        groups += 1

    return groups


if __name__ == '__main__':
    main()
