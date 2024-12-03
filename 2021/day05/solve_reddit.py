from collections import defaultdict

import parse

data = open('input.txt').readlines()

data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

def sign(foo):
    if foo < 0:
        return -1
    elif foo == 0:
        return 0
    return 1


points = defaultdict(int)
points_with_diags = defaultdict(int)

for line in data:
    sx, sy, ex, ey = tuple(parse.parse('{:d},{:d} -> {:d},{:d}', line).fixed)
    print(f"{sx},{sy} -> {ex},{ey}")
    l1 = abs(ex - sx)
    l2 = abs(ey - sy)
    s1 = sign(ex - sx)
    s2 = sign(ey - sy)
    print(f"lx: {l1}, ly: {l2}, s: {s1}:{s2}")
    print(list(range(max(l1, l2)+1)))
    for i in range(max(l1, l2) + 1):
        x, y = sx + s1 * i, sy + s2 * i
        points_with_diags[x, y] += 1
        if min(l1, l2) == 0:
            points[x, y] += 1

print(len([c for c in points if points[c] > 1]))
print(len([c for c in points_with_diags if points_with_diags[c] > 1]))
