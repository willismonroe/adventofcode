import day5
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day5Example(self):
        self.assertEqual(day5.solve('abc'), '18f47a30')

    def test_Day5Data(self):
        self.assertEqual(day5.solve('ugkcyxxp'), 'd4cd2ee1')

    def test_Day5_2Example(self):
        self.assertEqual(day5.decrypt('abc'), '05ace8e3')

    def test_Day2_5Data(self):
        self.assertEqual(day5.decrypt('ugkcyxxp'), 'f2c730e5')


if __name__ == '__main__':
    unittest.main()
