import collections
import re
import string

REGEX = re.compile(r'([a-z-]+?)-(\d+)\[([a-z]{5})\]')

class Room:
    def __init__(self, data):
        self.letters, self.sector_id, self.checksum = REGEX.match(data).groups()
        self.sector_id = int(self.sector_id)

    def validate(self):
        code = collections.Counter(''.join(c for c in self.letters if c in string.ascii_lowercase))
        top_letters = [(-n, c) for c, n in code.most_common()]
        ranked = ''.join(c for n, c in sorted(top_letters))
        if self.checksum == ranked[:5]:
            return True

    def translate(self):
        new_string = ''
        for letter in self.letters:
            if letter == '-':
                new_string += ' '
            else:
                new_string += chr(((ord(letter) - ord('a') + self.sector_id) % 26) + ord('a'))
        return new_string

def find_north_pole(data):
    for line in data:
        room = Room(line.strip())
        name = room.translate()
        if name.startswith('north'):
            return room.sector_id

def main(data):
    # data = ['roomcode\n', 'roomcode\n' ...]
    real_rooms = 0
    for line in data:
        room = Room(line.strip())
        if room.validate():
            real_rooms += room.sector_id
    return real_rooms

if __name__ == '__main__':
    data = []
    with open('input.txt') as f:
        data = f.readlines()
    print(main(data))
    print(find_north_pole(data))