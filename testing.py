import unittest
import main


class TestUnit(unittest.TestCase):
    def setUp(self):
        print('About to run a function')

    def test_main(self):
        test_num1 = 52
        test_num2 = 50
        result = main.sum_numbers(test_num1, test_num2)
        self.assertEqual(result, 102)

    def tearDown(self):
        print('Cleaning up the test...')


unittest.main()
