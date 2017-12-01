import hashlib


def solve(door_id):
    password = ''
    index = 1
    for a in range(8):
        new_char = 0
        while new_char == 0:
            new_char = 0
            hash = hashlib.md5(str.encode(door_id + str(index))).hexdigest()
            if hash[:5] == '00000':
                new_char = hash[5]
            index += 1
        password += new_char
    return password


def decrypt(door_id):
    password = list('________')
    int_index = 1
    for a in range(8):
        new_char = 0
        while new_char == 0:
            new_char = 0
            hash = hashlib.md5(str.encode(door_id + str(int_index))).hexdigest()
            if hash[:5] == '00000':
                if hash[5].isdigit():
                    if int(hash[5]) in range(8):
                        if password[int(hash[5])] == '_':
                            new_char = hash[6]
                            break
            int_index += 1
        password[int(hash[5])] = new_char
    return ''.join(password)


if __name__ == '__main__':
    # print(solve('ugkcyxxp'))
    print(decrypt('ugkcyxxp'))
