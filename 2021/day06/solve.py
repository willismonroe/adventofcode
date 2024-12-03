def main():
    raw_input = open('input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = "3,4,3,1,2"


def part1(raw_input):
    fish = list(map(int, raw_input.split(',')))
    for day in range(80):
        start_len = len(fish)
        for f in range(start_len):
            if fish[f] == 0:
                fish[f] = 6
                fish.append(8)
            else:
                fish[f] -= 1
    return len(fish)


def part2(raw_input):
    raw_fish = list(map(int, raw_input.split(',')))
    fish = {i: 0 for i in range(0, 9)}
    for f in raw_fish:
        fish[f] += 1
    for day in range(256):
        new_fish = {i: 0 for i in range(0, 9)}
        for d in range(0, 9):
            n_fish = fish[d]
            if d == 0:
                new_fish[6] += n_fish
                new_fish[8] += n_fish
            else:
                new_fish[d - 1] += fish[d]
        fish = new_fish
    return sum(fish.values())


if __name__ == "__main__":
    main()
