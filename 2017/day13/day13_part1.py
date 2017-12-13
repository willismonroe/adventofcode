import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day13_input.txt").read().splitlines()

    print(solve(input))


fw = {}


def check_collision(layer, depth):
    return layer % ((depth - 1) * 2) == 0


def solve(input):
    severity = 0
    for line in input:
        layer, depth = list(map(int, line.split(': ')))
        fw[layer] = depth
    for layer, depth in fw.items():
        if check_collision(layer, depth):
            severity += layer * depth

    return severity


if __name__ == '__main__':
    main()
