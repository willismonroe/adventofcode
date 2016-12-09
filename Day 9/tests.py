import day9
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day9_Example(self):
        string = 'ADVENT'
        self.assertEqual(day9.decompress(string), 6)

    def test_Day9_Example_2(self):
        string = 'A(1x5)BC'
        self.assertEqual(day9.decompress(string), 7)

    def test_Day9_Example_3(self):
        string = '(3x3)XYZ'
        self.assertEqual(day9.decompress(string), 9)

    def test_Day9_Example_4(self):
        string = 'A(2x2)BCD(2x2)EFG'
        self.assertEqual(day9.decompress(string), 11)

    def test_Day9_Example_5(self):
        string = 'A(2x2)BCD(2x2)EFG'
        self.assertEqual(day9.decompress(string), 11)

    def test_Day9_Example_6(self):
        string = '(6x1)(1x3)A'
        self.assertEqual(day9.decompress(string), 6)

    def test_Day9_Data(self):
        with open('input.txt') as f:
            data = f.read()
        self.assertEqual(day9.decompress(data), 138735)

    def test_Day9_2Example(self):
        string = '(3x3)XYZ'
        self.assertEqual(day9.decompress(string, True), 9)

    def test_Day9_2Example_2(self):
        string = 'X(8x2)(3x3)ABCY'
        self.assertEqual(day9.decompress(string, True), len('XABCABCABCABCABCABCY'))

    def test_Day9_2Example_3(self):
        string = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
        self.assertEqual(day9.decompress(string, True), 241920)

    def test_Day9_2Example_4(self):
        string = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
        self.assertEqual(day9.decompress(string, True), 445)

    def test_Day9_2_Data(self):
        with open('input.txt') as f:
            data = f.read()
        self.assertEqual(day9.decompress(data, True), 11125026826)


if __name__ == '__main__':
    unittest.main()
