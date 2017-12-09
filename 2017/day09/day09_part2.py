import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day09_input.txt").read()

    print(solve(input))


def solve(input):
    sum = 0
    index = 0
    nest = 0
    garbage = False
    garbage_sum = 0
    while index < len(input):
        cur = input[index]
        if cur == "!":
            index += 1
            garbage_sum -= 1
        elif cur == "<":
            garbage = True
        elif cur == ">":
            garbage = False
            garbage_sum -= 1
        elif garbage == False:
            if cur == "{":
                nest += 1
            elif cur == "}":
                sum += nest
                nest -= 1

        if garbage == True:
            garbage_sum += 1

        index += 1

    return garbage_sum


if __name__ == '__main__':
    main()
