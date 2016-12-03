def valid(triangle):
    # triangle = [d, d, d]
    triangle = sorted(triangle)
    if triangle[0] + triangle[1] > triangle[2]:
        return True
    else:
        return False

def main(data):
    num_valid = 0
    data = data.split('\n')
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        t1 = []
        t2 = []
        t3 = []
        for line in chunk:
            nums = list(map(int, line.split()))
            t1.append(nums[0])
            t2.append(nums[1])
            t3.append(nums[2])
        if valid(t1):
            num_valid += 1
        if valid(t2):
            num_valid += 1
        if valid(t3):
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    print(main(data))
