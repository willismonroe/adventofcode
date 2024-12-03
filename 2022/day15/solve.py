import pathlib
import re

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_input(inp):
    sensors = []
    beacons = set()
    for line in inp.splitlines():
        sx, sy, bx, by = map(int, re.findall(r"=(-?\d+)", line))
        d = manhattan([sx, sy], [bx, by])
        sensors.append([sx, sy, d])
        beacons.add((bx, by))
    return sensors, beacons


def part1(input, y=2000000):
    # y = 10
    sensors, beacons = parse_input(input)
    # should we factor in the distance here too?
    max_x = max([sensor[0] for sensor in sensors])
    max_x = max_x + max([s[2] for s in [s for s in sensors if s[0] == max_x]])
    min_x = min([sensor[0] for sensor in sensors])
    min_x = min_x - max([s[2] for s in [s for s in sensors if s[0] == min_x]])
    max_y = max([sensor[1] for sensor in sensors])
    min_y = min([sensor[1] for sensor in sensors])
    coverage = set()
    for sx, sy, d in sensors:
        # print("Sensor:", sx, sy, d)
        if manhattan([sx, sy], [sx, y]) <= d:
            # print("Within range")
            for x in range(sx-d, sx+d):
            # for x in range(min_x, max_x):
                if (x, y) in coverage:
                    continue
                # print("Checking point:", x, y)
                elif manhattan([sx, sy], [x, y]) <= d:
                    # print("Close enough:", manhattan([sx, sy], [x, y]))
                    coverage.add((x, y))
    # tmp = sorted(list(coverage), key=lambda a: a[0])
    # print(tmp)
    return len(coverage - beacons)


def part2(input):
    return 0


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
