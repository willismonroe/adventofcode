import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """125 17"""


def part1(puzzle_input: str) -> int:
    stones = list(map(int, puzzle_input.split()))
    blinks = 25
    for _ in range(blinks):
        new_stones: list[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[: len(str(stone)) // 2]))
                new_stones.append(int(str(stone)[len(str(stone)) // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)


def part2(puzzle_input: str) -> int:
    stones = {k: 1 for k in list(map(int, puzzle_input.split()))}
    blinks = 75
    for _ in range(blinks):
        new_stones: dict[int, int] = {}
        for key, value in stones.items():
            # print(key, value)
            if key == 0:
                new_stones[1] = new_stones.get(1, 0) + value
            elif len(str(key)) % 2 == 0:
                new_stones[int(str(key)[: len(str(key)) // 2])] = (
                    new_stones.get(int(str(key)[: len(str(key)) // 2]), 0)
                    + value
                )
                new_stones[int(str(key)[len(str(key)) // 2:])] = (
                    new_stones.get(int(str(key)[len(str(key)) // 2:]), 0)
                    + value
                )
            else:
                new_stones[key * 2024] = new_stones.get(key * 2024, 0) + value
        # print(new_stones)
        stones = new_stones
    return sum([v for v in stones.values()])


if __name__ == "__main__":
    with open(PUZZLE_DIR / "puzzle_input.txt") as f:
        puzzle_input = f.read()
    # puzzle_input = example_input
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
