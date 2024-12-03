def main():
    puzzle_input = open('part1_input.txt').read()
    print(solve(puzzle_input))


class Board:
    def __init__(self, lines) -> None:
        self.board = [[[int(n), 0] for n in line.split()] for line in lines]
    
    def pprint(self):
        for line in self.board:
            print(' '.join([str(c[0]) if c[1] == 0 else str(c[0])+"*" for c in line]))

    def mark(self, n):
        for line in self.board:
            for c in line:
                if c[0] == n:
                    c[1] = 1

    def sum_unmarked(self):
        sum = 0
        for line in self.board:
            for c in line:
                if c[1] == 0:
                    sum += c[0]
        return sum

    def check(self):
        for line in self.board:
            if ''.join([str(c[1]) for c in line]) == '11111':
                return True 
        for i in range(len(self.board[0])):
            if ''.join([str(line[i][1]) for line in self.board]) == '11111':
                return True

def solve(puzzle_input):
    lines = puzzle_input.splitlines()
    draw = lines[0].split(',')
    boards = []
    tmp_board = []
    for line in lines[2:]:
        if len(line) > 1:
            tmp_board.append(line)
        else:
            boards.append(Board(tmp_board))
            tmp_board = []
    boards.append(Board(tmp_board))

    for d in draw:
        print("Drawing:", d)
        for b in boards:
            b.mark(int(d))
        for b in boards:
            if b.check():
                print('Board won with guess:', d)
                return int(d) * b.sum_unmarked()






if __name__ == "__main__":
    main()