import day14
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day14_Example(self):
        self.assertEqual(day14.solve('abc'), 22728)

    def test_Day14_Data(self):
        self.assertEqual(day14.solve('ngcjuoqr'), 18626)

    def test_Day14_2_Example(self):
        self.assertEqual(day14.solve('abc', True), 22551)

    def test_Day14_2_Data(self):
        self.assertEqual(day14.solve('ngcjuoqr', True), 20092)

if __name__ == '__main__':
    unittest.main()
