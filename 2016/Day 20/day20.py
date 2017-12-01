from collections import deque

def solve(data, upper):
    sorted_intervals = deque(sorted([(int(start), int(end)) for line in data for start, end in [line.split('-')]], key=lambda x: x[0]))
    # [(0, 2), (4, 7), (5, 8)]
    answers = []
    total, n, index = 0, 0, 0
    while n < upper:
        start, end = sorted_intervals[index]
        if n >= start:
            if n <= end:
                n = end + 1
                continue
            index += 1
        else:
            total += 1
            answers.append(n)
            n += 1
    return total, sorted(answers)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    print(solve(data, 2**32))

    #data = ['5-8','0-2','4-7']
    #print(solve(data, 9))