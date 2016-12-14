import curses

def is_wall(x, y, data=1352):
    # x^2 + 3x + 2xy + y + y^2
    binary_sum = "{0:b}".format((x * x + 3 * x + 2 * x * y + y + y * y) + data)
    if binary_sum.count('1') % 2 == 1:
        return True
    else:
        return False

class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = is_wall(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def neighbors(self):
        cells = []

        # Top
        if self.y > 0:
            top = Cell(self.x, self.y - 1)
            if not top.wall:
                cells.append(top)
        # Left
        if self.x > 0:
            left = Cell(self.x - 1, self.y)
            if not left.wall:
                cells.append(left)
        # Right
        right = Cell(self.x + 1, self.y)
        if not right.wall:
            cells.append(right)
        # Bottom
        bottom = Cell(self.x, self.y + 1)
        if not bottom.wall:
            cells.append(bottom)

        return cells

def solve(start, end, screen=None):
    start = Cell(start[0], start[1])
    end = Cell(end[0], end[1])
    visited = [start]
    steps = 0
    next = visited
    part1 = None
    part2 = None
    while part1 is None or part2 is None:

        to_check = next.copy()
        next = []
        for cell in to_check:
            if screen:
                pp_screen(screen, visited, highlight=cell)
            for neighbor in cell.neighbors():
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                next.append(neighbor)
        steps += 1
        if end in next:
            part1 = steps
        # if steps == 50:
        #     part2 = len(visited)

    return part2

if __name__ == '__main__':
    screen = curses.initscr()

    print(solve((1,1), (31,39), screen))

