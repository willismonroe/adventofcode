import re

REGEX = re.compile('(?P<normal>[a-z]+)|(?P<hypernet>\[[a-z]+\])')

def is_ABA(string):
    # Look for ABA pattern in four letter string
    if string[0] == string[2]:
        return True
    else:
        return False

def find_ABAs(string):
    ABAs = []
    for i in range(len(string[:-2])):
        if is_ABA(string[i:i+3]):
            ABAs.append(string[i:i+3])
        else:
            pass
    return ABAs

def make_BAB(ABA):
    return ABA[1] + ABA[0] + ABA[1]

def solve(line):
    # line = 'ioxxoj[asdfgh]zxcvbn'
    groups = [m.groupdict() for m in REGEX.finditer(line)]
    # list of dicts for each match object
    # [{'hypernet': None, 'normal': 'ioxxoj'},
    # {'hypernet': '[asdfgh]', 'normal': None},
    # {'hypernet': None, 'normal': 'zxcvbn'}]
    valid = 0
    ABAs = []
    for group in groups:
        if group['normal']:
            for ABA in find_ABAs(group['normal']):
                ABAs.append(ABA)
    hABAs = []
    for group in groups:
        if group['hypernet']:
            for hABA in find_ABAs(group['hypernet']):
                hABAs.append(hABA)
    hABAs = [make_BAB(ABA) for ABA in hABAs]
    if list(set(ABAs) & set(hABAs)):
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