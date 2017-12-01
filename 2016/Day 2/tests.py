import day2, day2_2
import unittest

class Day2Tests(unittest.TestCase):

    def test_True(self):
        self.assertTrue(True)

    def test_Day2Example(self):
        input = '''ULL\nRRDDD\nLURDL\nUUUUD'''
        self.assertEqual(day2.main(input), '1985')

    def test_Day2Data(self):
        with open('input.txt') as f:
            # read the input file into lines
            # [[l,i,n,e,1],[l,i,n,e,2]...]
            file_input = f.read()
        self.assertEqual(day2.main(file_input), '78985')

    def test_Day2_2Example(self):
        input = '''ULL\nRRDDD\nLURDL\nUUUUD'''
        self.assertEqual(day2_2.main(input), '5DB3')

    def test_Day2_2Data(self):
        with open('input.txt') as f:
            # read the input file into lines
            # [[l,i,n,e,1],[l,i,n,e,2]...]
            file_input = f.read()
        self.assertEqual(day2_2.main(file_input), '57DD8')

if __name__ == '__main__':
    unittest.main()