import day19
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day19_Example(self):
        self.assertEqual(day19.solve(5), 3)


if __name__ == '__main__':
    unittest.main()
