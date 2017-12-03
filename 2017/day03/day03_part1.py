import math

def main():
    # solve for puzzle input
    input = int(open("day03_input.txt").read().strip())

    print(solve(input))

# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27 52
# 42  21  22  23  24  25  26 51
# 43  44  45  46  47  48  49 50


# 289326
def solve(input):
    if input == 1: return 0

    # find bottom right of square
    if math.ceil(math.sqrt(input)) % 2 == 0:
        bottom_right = math.ceil(math.sqrt(input)+1)**2
    else:
        bottom_right = math.ceil(math.sqrt(input))**2

    previous_bottom_right = math.floor((math.sqrt(bottom_right) - 2) ** 2)

    ring = math.floor((bottom_right-previous_bottom_right)/8)

    distance_on_ring = abs((bottom_right - input) % (ring*2) - ring)

    return ring + distance_on_ring


if __name__ == "__main__":
    main()