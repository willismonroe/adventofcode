import math

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
                slice = round(elf_num + len(ring)/2)
                #next_elf = next(i for i, v in enumerate(ring[elf_num + 1:] + ring[:elf_num]) if v > 0) + 1 + elf_num
                next_elf = next(i for i, v in enumerate(ring[slice:] + ring[:slice - 1]) if v > 0) + slice
                ring[elf_num] += ring[next_elf % len(ring)]
                ring[next_elf % len(ring)] = 0
    return ring

if __name__ == '__main__':
    data = 3005290
    data = 5

    print(solve_v2(data))