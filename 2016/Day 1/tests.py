import day1, day1_2
import unittest

class Day1Tests(unittest.TestCase):

    def test_True(self):
        self.assertTrue(True)

    def test_Day1Examples(self):
        self.assertEqual(day1.main("R2, L3"), 5)
        self.assertEqual(day1.main("R2, R2, R2"), 2)
        self.assertEqual(day1.main("R5, L5, R5, R3"), 12)

    def test_Day1Data(self):
        with open('input.txt') as f:
            # read in the data and split into instructions
            # ['L4', 'L3', 'R1' ...]
            data = f.read()
        self.assertEqual(day1.main(data), 332)

    def test_Day1_2Examples(self):
        self.assertEqual(day1_2.main("R8, R4, R4, R8"), 4)

    def test_Day1_2Data(self):
        with open('input.txt') as f:
            # read in the data and split into instructions
            # ['L4', 'L3', 'R1' ...]
            data = f.read()
        self.assertEqual(day1_2.main(data), 166)

if __name__ == '__main__':
    unittest.main()