import re

REGEX = re.compile("(\w+?|\w+?-\w+?) (generator|microchip)")

class Move:
    def __init__(self, parent, floors, elevator, load, direction):
        self.parent = parent
        self.floors = floors
        self.elevator = elevator
        self.load = load
        self.direction = direction

    def generate_moves(self):
        for floor in floors:

        return False

    def is_valid(self):
        valid = 0
        for floor in self.floors:
            generator = 0
            for object in floor:
                if object[1] == 'g':
                    generator = 1
            if generator:
                for object in floor:
                    if object[1] == 'm':
                        if object[0] + 'g' not in floor:
                            valid = 0
                valid = 1
            else:
                valid = 1
        return valid

class Building:
    def __init__(self, floors):
        self.floors = []
        self.count = 0
        self.elevator = 0
        for floor in floors:
            self.floors.append(self.parse_floor(floor))

    def parse_floor(self, floor_string):
        floor = []
        objects = REGEX.findall(floor_string)
        for object in objects:
            floor.append(''.join([object[0][0], object[1][0]]))
        return floor

    def fried(self, floor):
        generator = 0
        for object in floor:
            if object[1] == 'g':
                generator = 1
        if generator:
            for object in floor:
                if object[1] == 'm':
                    if object[0] + 'g' not in floor:
                        return True
            return False
        else:
            return False

    def print_floors(self):
        for floor in zip(range(len(self.floors))[::-1], self.floors[::-1]):
            print("#{} : {}".format(floor[0], ' '.join(floor[1])))

    def move(self, start, contents, direction):
        if direction not in [1,-1]:
            return False
        if start != self.elevator:
            return False
        dest = self.floors[start + direction]
        self.elevator = start + direction
        start = self.floors[start]
        # remove object from starting floor
        for object in contents:
            start.remove(object)
        # check validity of starting floor
        if self.fried(start):
            print("Removing {} fried the floor: {}".format(contents, start))
            start.append(contents)
            return False
        # add object to new floor
        for object in contents:
            dest.append(object)
        # check validity of new floor
        if self.fried(dest):
            print("Adding {} fried the floor: {}".format(contents, dest))
            for object in contents:
                dest.remove(object)
            return False
        self.count += 1
        return True

def solve(data):
    building = Building(data)
    for floor in building.floors:
        print(' '.join(floor))

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    #print(solve(data))
    # THIS IS IT:
    print(sum(2 * sum([4, 5, 1, 0][:x]) - 3 for x in range(1, 4)))
    print(sum(2 * sum([8, 5, 1, 0][:x]) - 3 for x in range(1, 4)))
