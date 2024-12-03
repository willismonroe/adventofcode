def main():
    puzzle_input = open('part1_input.txt').read()

    print(solve(puzzle_input))


def solve(puzzle_input):
    lines = puzzle_input.splitlines()
    binary = []
    for col in range(len(lines[0])):
        sum = 0
        for line in lines:
            sum += int(line[col])
        if sum > len(lines)/2:
            binary.append(1)
        else:
            binary.append(0)
    binary = ''.join([str(i) for i in binary])
    gamma = int(binary, 2)
    episolon = int(bin(int(binary, 2) ^ int('1'*len(binary), 2)), 2)
    return gamma * episolon


if __name__ == "__main__":
    main()