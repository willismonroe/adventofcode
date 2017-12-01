import day10
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day10_Example(self):
        data = ['value 5 goes to bot 2',
 'bot 2 gives low to bot 1 and high to bot 0',
 'value 3 goes to bot 1',
 'bot 1 gives low to output 1 and high to bot 0',
 'bot 0 gives low to output 2 and high to output 0',
 'value 2 goes to bot 2']
        self.assertEqual(day10.solve(data, ['2','5']), '2')

    def test_Day10_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day10.solve(data, ['17','61']), '157')

    def test_Day10_2_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day10.solve(data, part2=True), 1085)


if __name__ == '__main__':
    unittest.main()
