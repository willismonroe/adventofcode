import heapq

class Cell(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.f = 0
        self.h = 0

class AStar(object):
    def __init__(self, grid):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid = grid
        self.grid_height = len(grid)
        self.grid_width = len(grid[0])
        self.end = (0, 0)
        self.start = (0, 0)

    def load_cells(self):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                cell = Cell(x, y, self.grid[x][y] != '#')
                self.cells.append(cell)

    def get_heuristic(self, cell):
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x, y):
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        cells = []
        if cell.x < self.grid_width - 1:
            cells.append(self.get_cell(cell.x + 1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y - 1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x - 1, cell.y))
        if cell.y < self.grid_height - 1:
            cells.append(self.get_cell(cell.x, cell.y + 1))
        return cells

    def display_path(self):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            print("Path: cell: {},{}".format(cell.x, cell.y))

    def update_cell(self, adj, cell):
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def process(self):
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            f, cell = heapq.heappop(self.opened)
            self.closed.add(cell)
            if cell is self.end:
                self.display_path()
                break
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))


def solve(data):
    goals = []
    for y, line in enumerate(data):
        for x, l in enumerate(line):
            if l.isdigit():
                goals.append([l, (x, y)])
    astar = AStar(data)
    astar.load_cells()
    for goal in sorted(goals):


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [list(line) for line in f.read().splitlines()]

    print(solve(data))