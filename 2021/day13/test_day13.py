from day13.solve_day13 import part1, part2

example_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_part1():
    assert part1(example_input) == 17
    assert part1(open('day13_input.txt').read()) == 785


def test_part2():
    assert part2(example_input) == """
#####
#   #
#   #
#   #
#####
"""
    assert part2(open('day13_input.txt').read()) == """
####   ##  ##  #  #   ##  ##   ##  #  #
#       # #  # #  #    # #  # #  # #  #
###     # #  # ####    # #    #  # ####
#       # #### #  #    # # ## #### #  #
#    #  # #  # #  # #  # #  # #  # #  #
#     ##  #  # #  #  ##   ### #  # #  #
"""
