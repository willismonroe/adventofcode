import day13
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day13_Example(self):
        self.assertEqual(day13.solve((1,1),(7,4),data=10)[0], 11)

    def test_Day13_Data(self):
        self.assertEqual(day13.solve((1,1),(31,39))[0], 90)

    def test_Day13_Data_2(self):
        self.assertEqual(day13.solve((1,1),(31,39))[1], 135)

if __name__ == '__main__':
    unittest.main()
