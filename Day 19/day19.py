import math
import collections

def solve(data):
    ring = [1] * data
    solved = 0
    while not solved:
        if ring.count(len(ring)) == 1:
            solved = 1
            break
        for elf_num in range(len(ring)):
            elf = ring[elf_num]
            if elf == 0:
                pass
            else:
                next_elf = next(i for i, v in enumerate(ring[elf_num + 1:] + ring[:elf_num]) if v > 0) + 1 + elf_num
                ring[elf_num] += ring[next_elf % len(ring)]
                ring[next_elf % len(ring)] = 0
    return next(i for i, v in enumerate(ring) if v > 0) + 1

def solve(data):
    return (data - 2**math.floor(math.log(data, 2))) * 2 + 1

def solve_v2(data):
    left = collections.deque()
    right = collections.deque()
    for i in range(1, data+1):
        if i < (data // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)
    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]

def f(x):
    # this solves where x is not a power of 3, sort of
    a = math.floor(math.log(x, 3))
    b = x - 3**a
    c = math.floor(math.log(b, 3))
    d = b - 3**c
    return d


if __name__ == '__main__':
    data = 3005290
    data = 15

    print(solve_v2(data))

