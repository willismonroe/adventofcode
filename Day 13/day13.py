#http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/

import heapq
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
        """Initialize new cell.
        @param reachable is cell reachable? not a wall?
        @param x cell x coordinate
        @param y cell y coordinate
        @param g cost to move from the starting cell to this cell.
        @param h estimation of the cost to move from this cell
                 to the ending cell.
        @param f f = g + h
        """
        self.wall = is_wall(x, y)
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.h < other.h

class AStar(object):
    def __init__(self, start=(1,1), end=(31,39)):
        # open list
        self.opened = []
        heapq.heapify(self.opened)
        # visited cells list
        self.closed = set()
        # grid cells
        self.cells = {}
        self.start = Cell(start[0], start[1])
        self.end = Cell(end[0], end[1])

    def get_heuristic(self, cell):
        """Compute the heuristic value H for a cell.
        Distance between this cell and the ending cell multiply by 10.
        @returns heuristic value H
        """
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_adjacent_cells(self, cell):
        """Returns adjacent cells to a cell.
        Clockwise starting from the one on the right.
        @param cell get adjacent cells for this cell
        @returns adjacent cells list.
        """
        cells = []

        # Top
        if cell.y > 0:
            top = Cell(cell.x, cell.y-1)
            if not top.wall:
                cells.append(top)
        # Left
        if cell.x > 0:
            left = Cell(cell.x-1, cell.y)
            if not left.wall:
                cells.append(left)
        # Right
        right = Cell(cell.x+1, cell.y)
        if not right.wall:
            cells.append(right)
        # Bottom
        bottom = Cell(cell.x, cell.y+1)
        if not bottom.wall:
            cells.append(bottom)

        return cells

    def get_path(self):
        cell = self.end
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def update_cell(self, adj, cell):
        """Update adjacent cell.
        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self, screen=None):
        """Solve maze, find path to ending cell.
        @returns path or None if not found.
        """
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # pretty print current map
            #print("Current cell: {}x{}".format(cell.x, cell.y))
            #self.pprint(self.closed, cell)
            if screen:
                self.pprint_curses(screen, self.closed, cell)
            # if ending cell, return found path
            if cell is self.end:
                return self.get_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found
                        # for this adj cell.
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))

    def pprint(self, cells, highlight=None):
        grid = []
        xlim = sorted(cells, key=lambda cell: cell.x)[-1].x + 1
        ylim = sorted(cells, key=lambda cell: cell.y)[-1].y + 1
        for x in range(xlim):
            grid.append([])
            for y in range(ylim):
                grid[x].append(' ')
        for cell in cells:
            grid[cell.x][cell.y] = '.'
        print('  ' + ' '.join(map(str, [n % 10 for n in range(xlim + 1)])))
        for row, x in zip([n % 10 for n in range(ylim)], grid):
            print(str(row) + ' ' + ' '.join(x))
        if highlight:
            grid[highlight.x][highlight.y] = 'X'

    def pprint_curses(self, screen, cells, highlight=None):
        screen.clear()
        screen.move(0,0)
        grid = []
        xlim = sorted(cells, key=lambda cell: cell.x)[-1].x + 1
        ylim = sorted(cells, key=lambda cell: cell.y)[-1].y + 1
        for x in range(xlim):
            grid.append([])
            for y in range(ylim):
                grid[x].append(' ')
        for cell in cells:
            grid[cell.x][cell.y] = '.'
        screen.addstr('  ' + ' '.join(map(str, [n % 10 for n in range(xlim + 1)])) + '\n')
        for row, x in zip([n % 10 for n in range(ylim)], grid):
            screen.addstr(str(row) + ' ' + ' '.join(x) + '\n')
        if highlight:
            screen.addstr(cell.y, cell.x, 'O')
        screen.refresh()

if __name__ == '__main__':
    curses.setupterm()
    screen = curses.initscr()
    day13 = AStar()
    day13.solve(screen)

# count = 0
# visited = []
#
# def search(x, y, goal=(31, 39)):
#     global count
#     if (x, y) == goal:
#         print("Found after {} moves.".format(count))
#         return True
#     elif is_wall(x, y):
#         print("Wall at {}.".format((x, y)))
#         return False
#     elif (x, y) in visited:
#         print("Already visited {}.".format((x, y)))
#         return False
#
#     count += 1
#     visited.append((x, y))
#
#     if search(x + 1, y) or ( y > 0 and search(x, y - 1)) or (x > 0 and search(x - 1, y)) or search(x, y + 1):
#         return True
#     return False
#
# search(1,1)
