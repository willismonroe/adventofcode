import day16
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day16_Expand(self):
        self.assertEqual(day16.expand('1'), '100')
        self.assertEqual(day16.expand('0'), '001')
        self.assertEqual(day16.expand('11111'), '11111000000')
        self.assertEqual(day16.expand('111100001010'), '1111000010100101011110000')

    def test_Day16_Shrink(self):
        self.assertEqual(day16.shrink('110010110100'), '110101')
        self.assertEqual(day16.shrink('110101'), '100')

    def test_Day16_Example(self):
        self.assertEqual(day16.solve('10000', 20), '01100')

    def test_Day16_Data(self):
        self.assertEqual(day16.solve('11100010111110100', 272), '10100011010101011')

    def test_Day16_2_Data(self):
        self.assertEqual(day16.solve('11100010111110100', 35651584), '01010001101011001')

if __name__ == '__main__':
    unittest.main()
