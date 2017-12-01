import day3, day3_2
import unittest

class Day2Tests(unittest.TestCase):

    def test_True(self):
        self.assertTrue(True)

    def test_Day3Example(self):
        self.assertFalse(day3.valid([5, 10, 25]))

    def test_Day3Data(self):
        with open('input.txt') as f:
            data = f.read()
        self.assertEqual(day3.main(data), 917)

    def test_Day3_2Data(self):
        with open('input.txt') as f:
            data = f.read()
        self.assertEqual(day3_2.main(data), 1649)

if __name__ == '__main__':
    unittest.main()