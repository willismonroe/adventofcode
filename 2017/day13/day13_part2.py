import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day13_input.txt").read().splitlines()

    print(solve(input))


fw = {}


def check_collision(layer, depth):
    return layer % ((depth - 1) * 2) == 0


def solve(input):
    for line in input:
        layer, depth = list(map(int, line.split(': ')))
        fw[layer] = depth
    delay = 0
    while True:
        for layer, depth in fw.items():
            if check_collision(delay + layer, depth):
                break
        else:  # no break
            return delay
        delay += 1

    return delay

if __name__ == '__main__':
    main()
