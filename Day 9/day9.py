import re

REGEX = re.compile("\((\d+x\d+)\)")


def decompress(s):
    m = re.search("\((\d+)x(\d+)\)", s)
    if not m:
        return len(s)
    start = m.start(0)
    slice_len = int(m.group(1))
    times = int(m.group(2))
    i = start + len(m.group())
    return len(s[:start]) + len(s[i:i+slice_len]) * times + decompress(s[i+slice_len:])

def decompress_v2(s):
    m = re.search("\((\d+)x(\d+)\)", s)
    if not m:
        return len(s)
    start = m.start(0)
    slice_len = int(m.group(1))
    times = int(m.group(2))
    i = start + len(m.group())
    return len(s[:start]) + decompress_v2(s[i:i+slice_len]) * times + decompress_v2(s[i+slice_len:])


# Old method where I created the actual string
# def decompress(string, new_string=''):
#     print("Starting decompress with string: {}...".format(string[:40]))
#     if len(new_string) > 0:
#         print("Carried over new_string: {}...".format(new_string[:40]))
#     # Check for a match
#     m = REGEX.search(string)
#     if not m:
#         print("No matches in {}...".format(string[:40]))
#         new_string += string
#         print("**Final Output: {}.\n".format(new_string))
#         return new_string
#     # set up useful variables
#     slice_len, times = map(int, m.group(1).split('x'))
#     start, end = m.start(1)-1, m.end(1)+1
#     slice = string[end:end + slice_len]
#     # add anything before the first match
#     new_string += string[:start]
#     print("{} means repeat \"{}\" {} times".format(m.group(1), slice, times))
#     # add repeated text
#     new_string += slice * times
#     print("new_string: {}.".format(new_string))
#     # pass the rest to decompress again
#     print("Passing {} to decompress again.".format(string[end + slice_len:]))
#     return decompress(string[end + slice_len:], new_string)

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    print(decompress(data))
    print(decompress_v2(data))