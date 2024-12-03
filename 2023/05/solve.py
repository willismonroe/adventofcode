import pathlib
from collections import deque

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def part1(input):
    # input = example_input
    conversion: list[list[int]] = []
    raw_sections = input.split("\n\n")
    seeds = map(int, raw_sections[0].split(":")[1].split())
    end_locs = []
    for section in raw_sections[1:]:
        section_list = []
        for line in section.splitlines()[1:]:
            drs, srs, rl = map(int, line.split())
            section_list.append([drs, srs, rl])
        conversion.append(section_list)
    for seed in seeds:
        # print("start:", seed)
        # print("conversion:", conversion)
        for stage in conversion:
            for layer in stage:
                # print("layer:", layer)
                drs, srs, rl = layer
                if seed in range(srs, srs + rl):
                    seed = drs + seed - srs
                    break
            # print(seed)
        end_locs.append(seed)
    return min(end_locs)


def convert_part2(seed: int) -> int:
    return seed


def part2(input):
    # input = example_input
    mappings: list[list[int]] = []
    raw_sections = input.split("\n\n")
    segments = list(map(int, raw_sections[0].split(":")[1].split()))
    segments = deque(
        [(start, start + l) for start, l in zip(segments[0::2], segments[1::2])]
    )
    # print("seeds:", seeds)
    for section in raw_sections[1:]:
        section_list = []
        for line in section.splitlines()[1:]:
            drs, srs, rl = map(int, line.split())
            # [start, end, diff]
            section_list.append([srs, srs + rl, drs - srs])
        mappings.append(section_list)

    for mapping in mappings:
        processed = deque()
        while segments:
            a, b = segments.popleft()
            for c, d, delta in mapping:
                partial_left = c <= a < d
                partial_right = c < b <= d
                if partial_left and partial_right:
                    #                 # Complete overlap:
                    #                 #     a---b
                    #                 # c-----------d
                    processed.append((a + delta, b + delta))
                    break
                if partial_left:
                    #                 # Partial left overlap:
                    #                 #     a------b
                    #                 # c------d
                    processed.append((a + delta, d + delta))
                    segments.append((d, b))
                    break
                if partial_right:
                    #                 # Partial right overlap:
                    #                 # a------b
                    #                 #     c------d
                    processed.append((c + delta, b + delta))
                    segments.append((a, c))
                    break
                if a < c and b > d:
                    #                 # Partial inner overlap:
                    #                 # a-----------b
                    #                 #     c---d
                    processed.append((c + delta, d + delta))
                    segments.append((a, c))
                    segments.append((d, b))
                    break
            else:
                processed.append((a, b))

        segments = processed

    for mapping in mappings:
        processed = deque()

        while segments:
            a, b = segments.popleft()

            for c, d, delta in mapping:
                partial_left = c <= a < d
                partial_right = c < b <= d

                if partial_left and partial_right:
                    processed.append((a + delta, b + delta))
                    break

                if partial_left:
                    processed.append((a + delta, d + delta))
                    segments.append((d, b))
                    break

                if partial_right:
                    processed.append((c + delta, b + delta))
                    segments.append((a, c))
                    break

                if a < c and b > d:
                    processed.append((c + delta, d + delta))
                    segments.append((a, c))
                    segments.append((d, b))
                    break
            else:
                processed.append((a, b))

        segments = processed
    return min([x[0] for x in segments])


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
