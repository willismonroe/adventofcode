import day15
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day15_Example(self):
        data = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.""".splitlines()
        self.assertEqual(day15.solve(data), 5)

    def test_Day15_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()[:-1]
        self.assertEqual(day15.solve(data), 376777)

    def test_Day15_2_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day15.solve(data), 3903937)

if __name__ == '__main__':
    unittest.main()
