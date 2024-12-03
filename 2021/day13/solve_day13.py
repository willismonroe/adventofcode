def main():
    raw_input = open('day13_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def make_sheet(lines):
    sheet = set()
    for line in lines:
        if line == '':
            break

        coords = tuple(map(int, line.split(',')))
        sheet.add(coords)

    return sheet


def fold(sheet, axis, vertical=False):
    folded = set()
    for x, y in sheet:
        if vertical:
            if x > axis:
                x = axis - (x - axis)
        elif y > axis:
            y = axis - (y - axis)

        folded.add((x, y))
    return folded


def part1(raw_input):
    sheet = make_sheet(raw_input.splitlines())
    folds = [f.split()[-1] for f in raw_input.splitlines()[raw_input.splitlines().index('') + 1:]]
    for f in folds:
        dir, axis = f.split('=')
        axis = int(axis)
        sheet = fold(sheet, axis, 'x' in f)
        break
    return len(sheet)


def format_sheet(sheet):
    max_x = max(p[0] for p in sheet)
    max_y = max(p[1] for p in sheet)

    output = ''
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            output += '#' if (x, y) in sheet else ' '
        output += '\n'

    return output


def part2(raw_input):
    sheet = make_sheet(raw_input.splitlines())
    folds = [f.split()[-1] for f in raw_input.splitlines()[raw_input.splitlines().index('') + 1:]]
    for f in folds:
        dir, axis = f.split('=')
        axis = int(axis)
        sheet = fold(sheet, axis, 'x' in f)

    return '\n' + format_sheet(sheet)


if __name__ == "__main__":
    main()
