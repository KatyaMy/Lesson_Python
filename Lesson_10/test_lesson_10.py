import unittest

class TestMyCode(unittest.TestCase):

    def setUp(self) -> None:
        print('Starting testing: ')
        print('Set data or something else')

    def test_is_a_greater_than_b(self):
        a = 8
        b = 3
        self.assertTrue(a > b, f'{a} is not greater than {b}!')

    def test_x_is_equal_to_y(self):
        x = 45
        y = 45
        self.assertTrue(x == y, f'{x} is not equal to {y}')

    def tearDown(self) -> None:
        print('Clean date or do something else after the test')
        print('Testing is DONE!')

if __name__ == '__main__':
    unittest.main()