from numpy import matrix
from collections import Counter


def solve_most(data):
    # data = ['asdkfe', 'eisjgk', ... ]
    data = matrix([list(string) for string in data]).T
    # data = [['a','e' ...], ['s','i' ...
    message = ''
    for line in data:
        c = Counter(''.join(line.tolist()[0]))
        message += c.most_common(1)[0][0]
    return message


def solve_least(data):
    # data = ['asdkfe', 'eisjgk', ... ]
    data = matrix([list(string) for string in data]).T
    # data = [['a','e' ...], ['s','i' ...
    message = ''
    for line in data:
        c = Counter(''.join(line.tolist()[0]))
        message += c.most_common()[-1][0]
    return message


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    # print(solve_most(data))
    print(solve_least(data))
