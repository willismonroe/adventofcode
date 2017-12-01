

def invert(char):
    if char == '1':
        return '0'
    else:
        return '1'

def expand(string):
    return string + '0' + ''.join(list(map(invert, string[::-1])))

def shrink(string):
    chunks = [string[i:i + 2] for i in range(0, len(string), 2)]
    new_string = ''
    for chunk in chunks:
        if chunk in ['00', '11']:
            new_string += '1'
        else:
            new_string += '0'
    return new_string

def solve(data, length):
    while len(data) < length:
        data = expand(data)

    data = data[:length]

    checksum = shrink(data)
    while len(checksum) % 2 == 0:
        checksum = shrink(checksum)
    return checksum


if __name__ == '__main__':
    length = 272
    length = 35651584
    data = '11100010111110100'

    print(solve(data, length))