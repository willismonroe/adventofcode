import os


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input = open("day19_input.txt").read().splitlines()

    print(solve(input))

direction = {
    'N': (-1, 0, 'S'),
    'E': (0, 1, 'W'),
    'S': (1, 0, 'N'),
    'W': (0, -1, 'E')
}

def print_local(cell, m):
    for line in m[cell[0]-2:cell[0]+3]:
        l = []
        for column in line[cell[1]-2:cell[1]+3]:
            l.append(column)
        print(''.join(l))


def solve(input):
    m = [[c for c in l] for l in input]
    start = [0, m[0].index('|')]
    cur = start
    cur_dir = 'S'
    letters = []
    cur_cell = '|'
    steps = 0
    while cur_cell != 'H':
        cur_cell = m[cur[0]][cur[1]]
        if cur_cell.isalpha():
            # print(f"Found a letter: {cur_cell}")
            letters.append(cur_cell)
            cur[0] += direction[cur_dir][0]
            cur[1] += direction[cur_dir][1]
        elif cur_cell == '+':
            # print(f"Start: {cur_dir}")
            # print_local(cur, m)
            for next_dir in direction.keys():
                if next_dir not in [cur_dir, direction[cur_dir][2]]:
                    try:
                        next_cell = m[cur[0]+direction[next_dir][0]][cur[1]+direction[next_dir][1]]
                        if next_cell.isalpha() or next_cell in ['|','-']:
                            cur_dir = next_dir
                            break
                    except:
                        pass
            cur[0] += direction[cur_dir][0]
            cur[1] += direction[cur_dir][1]
            # print(f"End: {cur_dir}\n")
        else:
            cur[0] += direction[cur_dir][0]
            cur[1] += direction[cur_dir][1]
        steps += 1


    return steps

if __name__ == '__main__':
    main()
