import day1, day1_2
import unittest

class Day1Tests(unittest.TestCase):

    def test_Day1Examples(self):
        self.assertEqual(day1.main("R2, L3"), 5)
        self.assertEqual(day1.main("R2, R2, R2"), 2)
        self.assertEqual(day1.main("R5, L5, R5, R3"), 12)

if __name__ == '__main__':
    unittest.main()