import os
from collections import defaultdict

import day25_part1, day25_part2


def test_part1_example():
    tape = defaultdict(int)
    cur = 0

    def A(cur):
        if tape[cur] == 0:
            tape[cur] = 1
            cur += 1
            state = B
        else:
            tape[cur] = 0
            cur -= 1
            state = B
        return cur, state

    def B(cur):
        if tape[cur] == 0:
            tape[cur] = 1
            cur -= 1
            state = A
        else:
            tape[cur] = 1
            cur += 1
            state = A
        return cur, state

    state = A
    count = 0
    while count < 6:
        cur, state = state(cur)
        count += 1

    assert sum(tape.values()) == 3
