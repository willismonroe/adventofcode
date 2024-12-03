#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os

def test_file(day):
    return f"""from solve_{day} import part1, part2

example_input = \"\"\"\"\"\"

    
def test_part1_example():
    assert part1(example_input) == True

def test_part1():
    assert part1(open(\'{day}_input.txt\').read()) == True

def test_part2_example():
    assert part2(example_input) == True

def test_part2():
    assert part2(open(\'{day}_input.txt\').read()) == True
"""
    
def solve_file(day):
    return f"""

def main():
    raw_input = open(\'{day}_input.txt\').read()
    print(\"Part 1:\", part1(raw_input))
    print(\"Part 2:\", part2(raw_input))


example_input = \"\"\"\"\"\"


def part1(raw_input):
    return False


def part2(raw_input):
    return False


if __name__ == \"__main__\":
    main()
"""



def main():
    day = sys.argv[1]
    print("Making directory:")
    os.mkdir(day)
    print("Writing test file:")
    with open(f'{day}/test_{day}.py', 'w') as f:
        f.write(test_file(day))
    print("Writing input file:")
    with open(f'{day}/{day}_input.txt', 'w') as f:
        f.write('')
    print("Writing solve file:")
    with open(f'{day}/solve_{day}.py', 'w') as f:
        f.write(solve_file(day))
    print("Done!")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        sys.exit(0)
