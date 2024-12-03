import pytest
import solve

example_input_1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
example_input_2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
example_input_3 = """nppdvjthqldpwncqszvftbrmjlhg"""
example_input_4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
example_input_5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""



def test_part1():
    assert solve.part1(example_input_1) == 7
    assert solve.part1(example_input_2) == 5
    assert solve.part1(example_input_3) == 6
    assert solve.part1(example_input_4) == 10
    assert solve.part1(example_input_5) == 11


def test_part2():
    assert solve.part2(example_input_1) == 19
    assert solve.part2(example_input_2) == 23
    assert solve.part2(example_input_3) == 23
    assert solve.part2(example_input_4) == 29
    assert solve.part2(example_input_5) == 26