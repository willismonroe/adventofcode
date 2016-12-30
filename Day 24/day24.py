import heapq

# http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/

class Cell(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.f = 0
        self.h = 0

    def __lt__(self, other):
        return self.g < other.g

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

    def init_cells(self, start, end):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if self.grid[y][x] == '#':
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x, y, reachable))
        self.start = self.get_cell(start[0], start[1])
        self.end = self.get_cell(end[0], end[1])

    def get_heuristic(self, cell):
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x, y):
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        """
        Returns adjacent cells to a cell. Clockwise starting
        from the one on the right.

        @param cell get adjacent cells for this cell
        @returns adjacent cells list
        """
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
            print('path: cell: {},{}'.format(cell.x, cell.y))

    def count_path(self):
        cell = self.end
        count = 0
        while cell.parent is not self.start:
            cell = cell.parent
            count += 1
        return count

    def update_cell(self, adj, cell):
        """
        Update adjacent cell

        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def process(self):
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        count = 0
        while len(self.opened):
            #print(self.opened)
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, display found path
            if cell is self.end:
                #self.display_path()
                count += self.count_path()
                break
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found for this adj
                        # cell.
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))
        return count


def solve(data):
    goals = []
    for y, line in enumerate(data):
        for x, l in enumerate(line):
            if l.isdigit():
                goals.append([l, (x, y)])
    goals = sorted(goals)
    count = 0
    for i, goal in enumerate(goals[:-1]):
        start = (goal[1][0], goal[1][1])
        end = (goals[i+1][1][0], goals[i+1][1][1])
        astar = AStar(data)
        astar.init_cells(start, end)
        tmp_count = astar.process()
        count += tmp_count
        print("Steps from {}x{} to {}x{}: {}".format(start[0], start[1], end[0], end[1], tmp_count))
    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [list(line) for line in f.read().splitlines()]

    print(solve(data))