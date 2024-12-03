import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Time:      7  15   30
Distance:  9  40  200"""


def part1(input):
    # input = example_input
    races = list(
        zip(
            map(int, input.splitlines()[0].split(":")[1].split()),
            map(int, input.splitlines()[1].split(":")[1].split()),
        )
    )
    result = 1
    for race in races:
        ways_to_win = 0
        race_duration, record = race
        for button_time in range(race_duration + 1):
            if button_time * (race_duration - button_time) > record:
                ways_to_win += 1
        result *= ways_to_win
    return result


def part2(input):
    # input = example_input
    race_duration = int(input.splitlines()[0].split(":")[1].replace(" ", ""))
    record = int(input.splitlines()[1].split(":")[1].replace(" ", ""))
    print(race_duration, record)
    ways_to_win = 0
    for button_time in range(race_duration + 1):
        if button_time * (race_duration - button_time) > record:
            ways_to_win += 1
    return ways_to_win


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
