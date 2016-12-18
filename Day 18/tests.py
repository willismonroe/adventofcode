import day18
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day18_Example(self):
        data = '..^^.'
        rows = 3
        self.assertEqual(day18.solve(data, rows), 6)

    def test_Day18_Example_2(self):
        data = '.^^.^.^^^^'
        rows = 10
        self.assertEqual(day18.solve(data, rows), 38)

    def test_Day18_Data(self):
        data = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
        rows = 40
        self.assertEqual(day18.solve(data, rows), 1951)

    def test_Day18_2_Data(self):
        data = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
        rows = 400000
        self.assertEqual(day18.solve(data, rows), 20002936)

if __name__ == '__main__':
    unittest.main()
