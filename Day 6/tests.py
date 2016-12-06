import day6
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day6_Example(self):
        data = '''eedadn
        drvtee
        eandsr
        raavrd
        atevrs
        tsrnev
        sdttsa
        rasrtv
        nssdts
        ntnada
        svetve
        tesnvt
        vntsnd
        vrdear
        dvrsen
        enarar
        '''
        self.assertEqual(day6.solve_most(data.split()), 'easter')

    def test_Day6Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day6.solve_most(data), 'tsreykjj')

    def test_Day6_2Example(self):
        data = '''eedadn
        drvtee
        eandsr
        raavrd
        atevrs
        tsrnev
        sdttsa
        rasrtv
        nssdts
        ntnada
        svetve
        tesnvt
        vntsnd
        vrdear
        dvrsen
        enarar
        '''
        self.assertEqual(day6.solve_least(data.split()), 'advent')

    def test_Day6_2Data(self):
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day6.solve_least(data), 'hnfbujie')


if __name__ == '__main__':
    unittest.main()
