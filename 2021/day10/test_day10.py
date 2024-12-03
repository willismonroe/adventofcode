from day10.solve_day10 import part1, part2

example_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def test_part1():
    assert part1(example_input) == 26397
    assert part1(open('day10_input.txt').read()) == 399153


def test_part2():
    assert part2(example_input) == 288957
    assert part2(open('day10_input.txt').read()) == 2995077699
