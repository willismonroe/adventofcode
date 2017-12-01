import day12
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day12_Example(self):
        data = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".splitlines()
        self.assertEqual(day12.solve(data), 42)

    def test_Day12_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day12.solve(data), 318020)

    def test_Day12_2_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day12.solve(data, {'a': 0, 'b': 0, 'c': 1, 'd': 0}), 9227674)

if __name__ == '__main__':
    unittest.main()
