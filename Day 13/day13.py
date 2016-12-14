


class Cell(object):
    def __init__(self, x, y, data=1352):
        self.x = x
        self.y = y
        self.data = data
        self.wall = self.is_wall()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_wall(self):
        # x^2 + 3x + 2xy + y + y^2
        x, y = self.x, self.y
        binary_sum = "{0:b}".format((x * x + 3 * x + 2 * x * y + y + y * y) + self.data)
        if binary_sum.count('1') % 2 == 1:
            return True
        else:
            return False

    def neighbors(self):
        cells = []

        # Top
        if self.y > 0:
            top = Cell(self.x, self.y - 1, self.data)
            if not top.wall:
                cells.append(top)
        # Left
        if self.x > 0:
            left = Cell(self.x - 1, self.y, self.data)
            if not left.wall:
                cells.append(left)
        # Right
        right = Cell(self.x + 1, self.y, self.data)
        if not right.wall:
            cells.append(right)
        # Bottom
        bottom = Cell(self.x, self.y + 1, self.data)
        if not bottom.wall:
            cells.append(bottom)

        return cells

def solve(start, end, data=1352):
    start = Cell(start[0], start[1], data)
    end = Cell(end[0], end[1], data)
    visited = [start]
    steps = 0
    next = visited
    part1 = None
    part2 = None
    while part1 is None or part2 is None:

        to_check = next.copy()
        next = []
        for cell in to_check:

            for neighbor in cell.neighbors():
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                next.append(neighbor)
        steps += 1
        if end in next:
            part1 = steps
        if steps == 50:
            part2 = len(visited)

    return part1, part2

if __name__ == '__main__':

    print(solve((1,1), (31,39)))

