

def grab_three_above(index, previous_row):
    if index == 0:
        left = '.'
    else:
        left = previous_row[index - 1]
    center = previous_row[index]
    if index == len(previous_row) - 1 :
        right = '.'
    else:
        right = previous_row[index + 1]
    return ''.join([left, center, right])

def is_trap(three_above):
    if three_above in ['^^.', '.^^', '^..', '..^']:
        return True
    else:
        return False

def solve(data, rows):
    new_rows = [data]
    while len(new_rows) < rows:
        new_row = [[''] * len(new_rows[-1])][0]
        for col in range(len(new_rows[-1])):
            three_above = grab_three_above(col, new_rows[-1])
            if is_trap(three_above):
                new_row[col] = '^'
            else:
                new_row[col] = '.'
        new_rows.append(new_row)
    return sum([line.count('.') for line in [''.join(line) for line in new_rows]])


if __name__ == '__main__':
    first_line = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
    rows = 400000
    data = [chr for chr in first_line]

    print(solve(data, rows))