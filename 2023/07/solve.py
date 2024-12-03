import pathlib
from collections import Counter
from functools import cmp_to_key

PUZZLE_DIR = pathlib.Path(__file__).parent

example_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def compare_hands(h1, h2):
    scores = []
    for hand in [h1, h2]:
        c = Counter(hand)
        # print(hand, c)
        if len(c) == 1:
            # five of a kind
            scores.append(7)
        elif len(c) == 2 and c.most_common(1)[0][1] == 4:
            # four of a kind
            scores.append(6)
        elif len(c) == 2 and c.most_common(1)[0][1] == 3:
            # full house
            scores.append(5)
        elif len(c) == 3 and c.most_common(1)[0][1] == 3:
            # three of a kind
            scores.append(4)
        elif c.most_common(2)[0][1] == c.most_common(2)[1][1]:
            # two paid
            scores.append(3)
        elif len(c) == 4:
            # one pair
            scores.append(2)
        else:
            scores.append(1)
    if scores[0] < scores[1]:
        return -1
    elif scores[0] > scores[1]:
        return 1
    else:
        for a, b in zip(h1, h2):
            if rank.index(a) > rank.index(b):
                return 1
            elif rank.index(a) < rank.index(b):
                return -1


tbl = str.maketrans("TJQKA", "ABCDE")


def strength(hand):
    c = Counter(hand).values()
    freq = sorted(c, reverse=True)
    return (freq, hand)


def part1(input):
    # input = example_input
    hands = {
        line.split()[0].translate(tbl): int(line.split()[1])
        for line in input.splitlines()
    }
    score = 0
    hands2 = sorted(hands, key=strength)
    # for i, hand in enumerate(sorted(hands, key=cmp_to_key(compare_hands)), 1):
    #     score += i * hands[hand]
    for i, hand in enumerate(hands2, 1):
        score += i * hands[hand]
    return score


def strength_with_joker(hand):
    if hand == "00000":
        return [5], hand
    c = Counter(hand)
    js = c.pop("0", 0)
    freqs = sorted(c.values(), reverse=True)
    freqs[0] += js
    return freqs, hand


def part2(input):
    # input = example_input
    hands = {
        line.split()[0].translate(tbl): int(line.split()[1])
        for line in input.splitlines()
    }
    hands = {hand.replace("B", "0"): bet for hand, bet in hands.items()}
    # print(hands)
    score = 0
    hands2 = sorted(hands, key=strength_with_joker)
    # print(hands2)
    for i, hand in enumerate(hands2, 1):
        score += i * hands[hand]
    return score


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    # input = example_input
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
