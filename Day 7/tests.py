import day7, day7_2
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day7_Example(self):
        line = 'abba[mnop]qrst'
        self.assertTrue(day7.solve(line))

    def test_Day7_Example_2(self):
        line = 'abcd[bddb]xyyx'
        self.assertFalse(day7.solve(line))

    def test_Day7_Example_3(self):
        line = 'aaaa[qwer]tyui'
        self.assertFalse(day7.solve(line))

    def test_Day7_Example_4(self):
        line = 'ioxxoj[asdfgh]zxcvbn'
        self.assertTrue(day7.solve(line))

    def test_Day7_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day7.main(data), 115)

    def test_Day7_2_Example(self):
        line = 'aba[bab]xyz'
        self.assertTrue(day7_2.solve(line))

    def test_Day7_2_Example_2(self):
        line = 'xyx[xyx]xyx'
        self.assertFalse(day7_2.solve(line))

    def test_Day7_2_Example_3(self):
        line = 'aaa[kek]eke'
        self.assertTrue(day7_2.solve(line))

    def test_Day7_2_Example_4(self):
        line = 'zazbz[bzb]cdb'
        self.assertTrue(day7_2.solve(line))

    def test_Day7_Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day7_2.main(data), 231)

if __name__ == '__main__':
    unittest.main()
