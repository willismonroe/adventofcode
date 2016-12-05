import day4
import unittest

class Day2Tests(unittest.TestCase):

    def test_True(self):
        self.assertTrue(True)

    def test_Day4Example(self):
        room = day4.Room('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertTrue(room.validate())

    def test_Day4Example_2(self):
        room = day4.Room('a-b-c-d-e-f-g-h-987[abcde]')
        self.assertTrue(room.validate())

    def test_Day4Example_3(self):
        room = day4.Room('not-a-real-room-404[oarel]')
        self.assertTrue(room.validate())

    def test_Day4Example_4(self):
        room = day4.Room('totally-real-room-200[decoy]')
        self.assertFalse(room.validate())

    def test_Day4Data(self):
        data = []
        with open('input.txt') as f:
            data = f.readlines()
        self.assertEqual(day4.main(data), 409147)

    def test_Day4_2Example(self):
        room = day4.Room('qzmt-zixmtkozy-ivhz-343[abcde]')
        self.assertEqual(room.translate(), 'very encrypted name')

    def test_Day4_2Data(self):
        data = []
        with open('input.txt') as f:
            data = f.readlines()
        self.assertEqual(day4.find_north_pole(data), 991)

if __name__ == '__main__':
    unittest.main()