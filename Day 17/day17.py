from hashlib import md5
from itertools import compress
from collections import deque


def get_doors(data, path):
    string = (data + ''.join(path)).encode('utf-8')
    return (int(x, 16) > 10 for x in md5(string).hexdigest()[:4])

def solve(data):
    start = (0,0)
    end = (3,3)

    moves = {
        'U': lambda x, y: (x, y - 1),
        'D': lambda x, y: (x, y + 1),
        'L': lambda x, y: (x - 1, y),
        'R': lambda x, y: (x + 1, y)
    }

    queue = deque([(start, [start], [])])
    while queue:
        (x, y), path, dirs = queue.popleft()
        for dir in compress('UDLR', get_doors(data, dirs)):
            next = moves[dir](x, y)
            nx, ny = next
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            elif next == end:
                yield dirs + [dir]
            else:
                queue.append((next, path + [next], dirs + [dir]))


if __name__ == '__main__':
    data = 'gdjjyniy'

    paths = list(solve(data))
    print(''.join(paths[0]), len(paths[-1]))