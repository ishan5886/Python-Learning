import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):   #Make sure tests start with the word 'test' else error will be presented
        result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)


if __name__ == '__main__':
    unittest.main()


