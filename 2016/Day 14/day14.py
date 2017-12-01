from hashlib import md5
import re
import functools

re_3 = re.compile(r'(.)\1{2}')
re_5 = '({})\1{4}'

@functools.lru_cache(maxsize=2048)
def get_hash(hash, stretch=False):
    if stretch:
        for n in range(2017):
            hash = get_hash(hash)
    else:
        hash = md5(str.encode(hash)).hexdigest()
    return hash

def solve(salt, stretch=False):
    keys = []
    i = 0
    while len(keys) < 64:
        hash = get_hash(salt + str(i), stretch)
        if re_3.search(hash):
            character = re_3.search(hash).group()[0]
            re_5 = re.compile(r'(' + character + r')\1{4}')
            tmp_int = i + 1
            while tmp_int - i < 1000:
                second_hash = get_hash(salt + str(tmp_int), stretch)
                if re_5.search(second_hash):
                    keys.append((hash, i))
                    break
                tmp_int += 1
        i += 1
    return i - 1

def solve_v2(salt, stretch=False):
    keys = []
    i = 0
    hashes = [get_hash(salt + str(n), stretch) for n in range(1000)]
    while len(keys) < 64:
        hash = hashes[i]
        if re_3.search(hash):
            character = re_3.search(hash).group()[0]
            re_5 = re.compile(r'(' + character + r')\1{4}')
            tmp_int = i + 1
            while tmp_int -i < 1000:
                second_hash = hashes[tmp_int]
                if re_5.search(second_hash):
                    keys.append((hash, i))
                    break
                tmp_int += 1
        hashes.append(get_hash(salt + str(i + 1000), stretch))
        i += 1
    return i - 1

if __name__ == '__main__':
    salt = 'ngcjuoqr'
    salt = 'abc'

    print(solve_v2(salt, True))