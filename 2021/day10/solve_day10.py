def main():
    raw_input = open('day10_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


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

open_signs = ['(', '[', '{', '<']
close_signs = [')', ']', '}', '>']


def balance(line):
    stack = []
    for char in line:
        if char in open_signs:
            stack.append(char)
        elif char in close_signs:
            i = close_signs.index(char)
            if len(stack) > 0 and open_signs[i] == stack[-1]:
                stack.pop()
            else:
                return char
    if len(stack) == 0:
        return True
    else:
        return stack


def part1(raw_input):
    lines = raw_input.splitlines()
    # (, [, }, <
    error = 0
    for line in lines:
        char = balance(line)
        if char == ')':
            error += 3
        elif char == ']':
            error += 57
        elif char == '}':
            error += 1197
        elif char == '>':
            error += 25137

    return error


def part2(raw_input):
    lines = raw_input.splitlines()
    scores = []
    for line in lines:
        result = balance(line)
        if type(result) == list:
            closing_string = []
            score = 0
            for char in result[::-1]:
                i = open_signs.index(char)
                closing_string.append(close_signs[i])
            for char in closing_string:
                score *= 5
                if char == ')':
                    score += 1
                elif char == ']':
                    score += 2
                elif char == '}':
                    score += 3
                elif char == '>':
                    score += 4
            scores.append(score)
    scores = sorted(scores)
    return scores[len(scores) // 2]


if __name__ == "__main__":
    main()
