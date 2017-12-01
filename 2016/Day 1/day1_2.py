def main(data):
    cur_loc = [0, 0]
    facing = 0

    gazetteer = [cur_loc[:]]

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
                return distance_from_origin

            gazetteer.append(cur_loc[:])

    total_distance = abs(cur_loc[0]) + abs(cur_loc[1])

    return total_distance


if __name__ == '__main__':
    with open('input.txt') as f:
        # read in the data and split into instructions
        # ['L4', 'L3', 'R1' ...]
        data = f.read()
    print(main(data))
