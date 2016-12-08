import day8
import unittest


class Day2Tests(unittest.TestCase):
    def test_True(self):
        self.assertTrue(True)

    def test_Day8_Example(self):
        answer = [['#', '#', '#', '.', '.', '.', '.'],
                  ['#', '#', '#', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.']]
        screen = day8.Screen(7, 3)
        screen.parse_line('rect 3x2')
        self.assertTrue((screen.screen == answer).all())

    def test_Day8_Example_2(self):
        answer = [['#', '.', '#', '.', '.', '.', '.'],
                  ['#', '#', '#', '.', '.', '.', '.'],
                  ['.', '#', '.', '.', '.', '.', '.']]
        screen = day8.Screen(7, 3)
        screen.parse_line('rect 3x2')
        screen.parse_line('rotate column x=1 by 1')
        self.assertTrue((screen.screen == answer).all())

    def test_Day8_Example_3(self):
        answer = [['.', '.', '.', '.', '#', '.', '#'],
                  ['#', '#', '#', '.', '.', '.', '.'],
                  ['.', '#', '.', '.', '.', '.', '.']]
        screen = day8.Screen(7, 3)
        screen.parse_line('rect 3x2')
        screen.parse_line('rotate column x=1 by 1')
        screen.parse_line('rotate row y=0 by 4')
        self.assertTrue((screen.screen == answer).all())

    def test_Day8_Example_4(self):
        answer = [['.', '#', '.', '.', '#', '.', '#'],
                  ['#', '.', '#', '.', '.', '.', '.'],
                  ['.', '#', '.', '.', '.', '.', '.']]
        screen = day8.Screen(7, 3)
        screen.parse_line('rect 3x2')
        screen.parse_line('rotate column x=1 by 1')
        screen.parse_line('rotate row y=0 by 4')
        screen.parse_line('rotate column x=1 by 1')
        self.assertTrue((screen.screen == answer).all())

    def test_Day8_Data(self):
        screen = day8.Screen(50, 6)
        with open('input.txt') as f:
            data = f.read().splitlines()
        self.assertEqual(day8.solve(screen, data), 110)


if __name__ == '__main__':
    unittest.main()
