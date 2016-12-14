from hashlib import md5
import re
import functools

re_3 = re.compile(r'(.)\1{2}')
re_5 = '({})\1{4}'

@functools.lru_cache(maxsize=2048)
def get_hash(string):
    return md5(str.encode(string)).hexdigest()

@functools.lru_cache(maxsize=2048)
def stretch_hash(hash):
    for n in range(2016):
        hash = get_hash(hash)
    return hash

def solve(salt, stretch=False):
    keys = []
    i = 0
    while len(keys) < 64:
        if stretch:
            hash = stretch_hash(get_hash(salt + str(i)))
        else:
            hash = get_hash(salt + str(i))
        if re_3.search(hash):
            character = re_3.search(hash).group()[0]
            re_5 = re.compile(r'(' + character + r')\1{4}')
            tmp_int = i + 1
            while tmp_int - i < 1000:
                if stretch:
                    second_hash = stretch_hash(get_hash(salt + str(tmp_int)))
                else:
                    second_hash = get_hash(salt + str(tmp_int))
                if re_5.search(second_hash):
                    keys.append((hash, i))
                    break

                tmp_int += 1
        i += 1
    return i - 1

if __name__ == '__main__':
    salt = 'ngcjuoqr'
    #salt = 'abc'

    print(solve(salt, True))