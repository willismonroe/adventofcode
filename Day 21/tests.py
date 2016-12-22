import day21
import unittest

class Day2Tests(unittest.TestCase):

    def test_True(self):
        self.assertTrue(True)

    def test_Day21_Example_swap_pos(self):
        scrambler = day21.Scramble('abcde')
        line = 'swap position 4 with position 0'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'ebcda')

    def test_Day21_Example_swap_let(self):
        scrambler = day21.Scramble('ebcda')
        line = 'swap letter d with letter b'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'edcba')

    def test_Day21_Example_reverse(self):
        scrambler = day21.Scramble('edcba')
        line = 'reverse positions 0 through 4'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'abcde')

    def test_Day21_Example_rotate_left(self):
        scrambler = day21.Scramble('abcde')
        line = 'rotate left 1 step'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'bcdea')

    def test_Day21_Example_move_pos(self):
        scrambler = day21.Scramble('bcdea')
        line = 'move position 1 to position 4'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'bdeac')

    def test_Day21_Example_move_pos_2(self):
        scrambler = day21.Scramble('bdeac')
        line = 'move position 3 to position 0'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'abdec')

    def test_Day21_Example_rotate_based(self):
        scrambler = day21.Scramble('abdec')
        line = 'rotate based on position of letter b'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'ecabd')

    def test_Day21_Example_rotate_based_2(self):
        scrambler = day21.Scramble('ecabd')
        line = 'rotate based on position of letter d'
        scrambler.parse(line)
        self.assertEqual(scrambler, 'decab')

    def test_Day21_Example(self):
        with open('test_input.txt') as f:
            data = f.read().splitlines()
        start = 'abcde'
        self.assertEqual(day21.solve(start, data), 'decab')

    def test_Day21_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        start = 'abcdefgh'
        self.assertEqual(day21.solve(start, data), 'gcedfahb')

    def test_Day21_Data_2(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        start = 'fbgdceah'
        self.assertEqual(day21.solve_v2(start, data), 'hegbdcfa')


if __name__ == '__main__':
    unittest.main()