def press(keypad, loc):
    return keypad[loc[0]][loc[1]]

def main(input):
    data = []

    for line in input.split('\n'):
        data.append(list(line))

    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    location = [1, 1]

    answer = []

    for line in data:
        # line = ['U','U','L','D'...
        for direction in line:
            # direction = 'U'

            # compute new direction
            if direction == 'U':
                location[0] -= 1
            elif direction == 'R':
                location[1] += 1
            elif direction == 'D':
                location[0] += 1
            elif direction == 'L':
                location[1] -= 1

            # check out of bounds
            if location[0] < 0:
                location[0] = 0
            if location[1] < 0:
                location[1] = 0
            if location[0] > 2:
                location[0] = 2
            if location[1] > 2:
                location[1] = 2

        answer.append(press(keypad, location))

    return ''.join(str(n) for n in answer)

if __name__ == '__main__':
    with open('input.txt') as f:
        # read the input file into lines
        # [[l,i,n,e,1],[l,i,n,e,2]...]
        data = f.read()

    print(main(data))
