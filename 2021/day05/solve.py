def main():
    raw_input = open('input.txt').read()
    print(part1(raw_input))
    print(part2(raw_input))


def pprint(board):
    max_x = max(board.keys())
    max_y = max([max(board[x].keys()) for x in board.keys()])
    for y in range(max_y + 1):
        print(y, ''.join([str(board[x].get(y, 0)) for x in range(max_x + 1)]))


def construct_board(raw_input, diagonal=False):
    points = [[list(map(int, p.split(','))) for p in line.split(' -> ')] for line in raw_input.splitlines()]
    board = {}
    for p in [p for line in points for p in line]:
        if p[0] in board:
            board[p[0]][p[1]] = 0
        else:
            board[p[0]] = {p[1]: 0}
    for line in points:
        if line[0][0] == line[1][0]:
            d_y = abs(line[1][1] - line[0][1])
            min_y = min(line[1][1], line[0][1])
            x = line[0][0]
            for i in range(d_y + 1):
                try:
                    board[x][min_y + i] += 1
                except KeyError:
                    board[x][min_y + i] = 1
        elif line[0][1] == line[1][1]:
            d_x = abs(line[1][0] - line[0][0])
            min_x = min(line[1][0], line[0][0])
            y = line[0][1]
            for i in range(d_x + 1):
                try:
                    board[min_x + i][y] += 1
                except KeyError:
                    try:
                        board[min_x + i][y] = 1
                    except KeyError:
                        board[min_x + i] = {y: 1}
        elif diagonal:
            if abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
                l = max(abs(line[0][0] - line[1][0]), abs(line[0][1] - line[1][1]))
                d_x = int((line[1][0] - line[0][0]) / l)
                d_y = int((line[1][1] - line[0][1]) / l)
                for p in range(l + 1):
                    x = line[0][0] + p * d_x
                    y = line[0][1] + p * d_y
                    try:
                        board[x][y] += 1
                    except KeyError:
                        try:
                            board[x][y] = 1
                        except KeyError:
                            board[x] = {y: 1}


        else:
            pass
    return board


def part1(raw_input):
    board = construct_board(raw_input)
    result = 0
    for x in board.keys():
        result += len([value for value in board[x].values() if value > 1])
    return result


def part2(raw_input):
    board = construct_board(raw_input, diagonal=True)
    result = 0
    for x in board.keys():
        result += len([value for value in board[x].values() if value > 1])
    return result


if __name__ == "__main__":
    main()
