import os
from collections import defaultdict


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inp = open("day25_input.txt").read().splitlines()

    print(solve(inp))


RIGHT = 1
LEFT = -1

def solve(inp):
    tape = defaultdict(int)
    cur = 0

    def A(cur):
        if tape[cur] == 0:
            tape[cur] = 1
            cur += RIGHT
            state = B
        elif tape[cur] == 1:
            tape[cur] = 0
            cur += LEFT
            state = F
        return cur, state

    def B(cur):
        if tape[cur] == 0:
            tape[cur] = 0
            cur += RIGHT
            state = C
        elif tape[cur] == 1:
            tape[cur] = 0
            cur += RIGHT
            state = D
        return cur, state

    def C(cur):
        if tape[cur] == 0:
            tape[cur] = 1
            cur += LEFT
            state = D
        elif tape[cur] == 1:
            tape[cur] = 1
            cur += RIGHT
            state = E
        return cur, state

    def D(cur):
        if tape[cur] == 0:
            tape[cur] = 0
            cur += LEFT
            state = E
        elif tape[cur] == 1:
            tape[cur] = 0
            cur += LEFT
            state = D
        return cur, state

    def E(cur):
        if tape[cur] == 0:
            tape[cur] = 0
            cur += RIGHT
            state = A
        elif tape[cur] == 1:
            tape[cur] = 1
            cur += RIGHT
            state = C
        return cur, state

    def F(cur):
        if tape[cur] == 0:
            tape[cur] = 1
            cur += LEFT
            state = A
        elif tape[cur] == 1:
            tape[cur] = 1
            cur += RIGHT
            state = A
        return cur, state

    state = A
    count = 0
    while count < 12994925:
        cur, state = state(cur)
        count += 1


    return sum(tape.values())


if __name__ == '__main__':
    main()
