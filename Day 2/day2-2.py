with open('input.txt') as f:
    # read the input file into lines
    # [[l,i,n,e,1],[l,i,n,e,2]...]
    data = []
    for line in f.readlines():
        data.append(list(line))


keypad = [[0,0,1,0,0],
          [0,2,3,4,0],
          [5,6,7,8,9],
          [0,'A','B','C',0],
          [0,0,'D',0,0]]

location = [2,0]

data = [list(line) for line in '''
ULL
RRDDD
LURDL
UUUUD
'''.split()]

def press(loc):
    return keypad[loc[0]][loc[1]]

for line in data:
    # line = ['U','U','L','D'...
    for direction in line:
        # direction = 'U'
        print("\nStarting at: {}, over button: {}".format(location, press(location)))
        print("Instructions are: {}".format(direction))

        new_location = location

        # compute new direction
        if direction == 'U':
            new_location[0] -= 1
        elif direction == 'R':
            new_location[1] += 1
        elif direction == 'D':
            new_location[0] += 1
        elif direction == 'L':
            new_location[1] -= 1

        print("Location is now: {}".format(location))

        # check out of bounds
        if new_location[0] < 0: new_location[0] = 0
        if new_location[1] < 0: new_location[1] = 0
        if new_location[0] > 4: new_location[0] = 4
        if new_location[1] > 4: new_location[1] = 4

        print("Which takes us to: {}, over button: {}".format(new_location, press(new_location)))

        # if we run into a 0 stay put
        if press(new_location) == 0:
            print("But that's over a zero, so we return to: {}".format(location))
            new_location = location
        else:
            location = new_location


    print(press(location))