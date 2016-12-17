from hashlib import md5

class Room:
    def __init__(self, loc, path, parent):
        self.loc = loc
        self.path = path
        self.parent = parent

    def neighbors(self, hash):
        hash = md5(str.encode(hash + self.path)).hexdigest()
        doors = []
        for char in hash[:4]:
            if char in ['b','c','d','e','f']:
                doors.append(1)
            else:
                doors.append(0)
        return doors

def solve(data):

    loc = (0,0)
    end = (3,3)
    path = ''

    current = Room(loc, path, None)
    visited = [current]
    next = visited
    while loc not end:
        loc = current.loc
        to_check = next.copy()
        next = []
        for cell in to_check:



if __name__ == '__main__':
    data = 'gdjjyniy'

    print(solve(data))