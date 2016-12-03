def valid(triangle):
    # triangle = [d, d, d]
    if triangle[0] + triangle[1] > triangle[2]:
        if triangle[1] + triangle[2] > triangle[0]:
            if triangle[0] + triangle[2] > triangle[1]:
                return True
    else:
        return False

def main(data):
    num_valid = 0
    for line in data.split('\n'):
        triangle = list(map(int, line.split()))
        if valid(triangle):
            num_valid += 1

    return num_valid

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    print(main(data))
