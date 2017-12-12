import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day12_input.txt").read().splitlines()

    print(solve(input))


villages = {}


def count_pipes(village, seen):
    seen = []

    def linked_pipes(village):
        pipes = villages[village]
        for pipe in pipes:
            if pipe not in seen:
                seen.append(pipe)
                linked_pipes(pipe)

    linked_pipes(village)
    return len(seen)


def solve(input):
    for line in input:
        village, pipes = line.split(' <-> ')
        pipes = pipes.split(', ')
        villages[village] = pipes

    return count_pipes('0', seen=[])


if __name__ == '__main__':
    main()
