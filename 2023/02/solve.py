import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def part1(input):
    r_max = 12
    g_max = 13
    b_max = 14
    possible_sum = 0
    for line in input.splitlines():
        # print(line)
        game_num, rounds = line.split(':')
        game_num = int(game_num.split()[1])
        valid = True
        for round in rounds.split(';'):
            # print(round)
            for grab in round.split(','):
                num, color = grab.split()
                match color:
                    case 'red':
                        if int(num) > r_max:
                            valid = False
                    case 'green':
                        if int(num) > g_max:
                            valid = False
                    case 'blue':
                        if int(num) > b_max:
                            valid = False
                if not valid:
                    break
            if not valid:
                break
        if valid:
            # print("√", possible_sum, game_num)
            possible_sum += game_num
            # print(possible_sum)
    return possible_sum


def part2(input):
    game_mins = []
    for line in input.splitlines():
        r_min = 0
        g_min = 0
        b_min = 0
        # print(line)
        game_num, rounds = line.split(':')
        game_num = int(game_num.split()[1])
        for round in rounds.split(';'):
            # print(round)
            for grab in round.split(','):
                num, color = grab.split()
                match color:
                    case 'red':
                        if int(num) > r_min:
                            r_min = int(num)
                    case 'green':
                        if int(num) > g_min:
                            g_min = int(num)
                    case 'blue':
                        if int(num) > b_min:
                            b_min = int(num)
        game_mins.append(r_min*g_min*b_min)
    return sum(game_mins)


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
