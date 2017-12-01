import re

REGEX = re.compile('(?P<normal>[a-z]+)|(?P<hypernet>\[[a-z]+\])')

def is_ABBA(string):
    # Look for ABBA pattern in four letter string
    if string[:2] == string[2:][::-1] and string[0] != string[1]:
        return True
    else:
        return False

def find_ABBA(string):
    for i in range(len(string[:-3])):
        if is_ABBA(string[i:i+4]):
            return True
        else:
            pass
    return False

def solve(line):
    # line = 'ioxxoj[asdfgh]zxcvbn'
    groups = [m.groupdict() for m in REGEX.finditer(line)]
    # list of dicts for each match object
    # [{'hypernet': None, 'normal': 'ioxxoj'},
    # {'hypernet': '[asdfgh]', 'normal': None},
    # {'hypernet': None, 'normal': 'zxcvbn'}]
    valid = 0
    for group in groups:
        if group['hypernet']:
            if find_ABBA(group['hypernet']):
                return False
        elif group['normal']:
            if find_ABBA(group['normal']):
                valid = 1
    if valid:
        return True
    else:
        return False


def main(data):
    total = 0
    for line in data:
        if solve(line):
            total += 1
    return total

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    print(main(data))