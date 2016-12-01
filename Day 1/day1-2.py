import sys

with open('input.txt') as f:
    # read in the data and split into instructions
    # ['L4', 'L3', 'R1' ...]
    data = f.read()

start = [0, 0]
cur_loc = [0, 0]
facing = 0
# dictionary for pretty printing our messages
directions = {0: 'North', 90: 'East', 180: 'South', 270: 'West'}

gazetteer = [start]

for instruction in data.split(', '):
    # find out which direction we're facing after turning
    # 0 = North, 90 = East, 180 = South, 270 = West
    if instruction[0] == 'R':
        facing = (facing + 90) % 360
    elif instruction[0] == 'L':
        facing = (facing - 90) % 360

    # get the number of blocks from the instructions
    distance = int(instruction[1:])

    # move our location that many blocks in the correct direction, record each step
    for step in range(distance):
        if facing == 0:
            cur_loc[1] -= 1
        elif facing == 90:
            cur_loc[0] += 1
        elif facing == 180:
            cur_loc[1] += 1
        elif facing == 270:
            cur_loc[0] -= 1

        distance_from_origin = abs(cur_loc[0]) + abs(cur_loc[1])

        if cur_loc in gazetteer:
            print("{}: We moved {} {} blocks and are now at: {}.".format(instruction,
                                                                         directions[
                                                                             facing],
                                                                         distance,
                                                                         cur_loc,
                                                                         distance_from_origin,
                                                                         start))
            print("We've been here before, we're {} blocks from {}.".format(distance_from_origin, start))
            sys.exit(0)

        gazetteer.append(cur_loc[:])

    distance_from_origin = abs(cur_loc[0]) + abs(cur_loc[1])

    print("{}: We moved {}, {} blocks and are now at: {} a distance of {} blocks from {}".format(instruction,
                                                                                                 directions[facing],
                                                                                                 distance, cur_loc,
                                                                                                 distance_from_origin,
                                                                                                 start))

total_distance = abs(cur_loc[0]) + abs(cur_loc[1])
print("Total distance from {} to {} is: {}".format(start, cur_loc, total_distance))
