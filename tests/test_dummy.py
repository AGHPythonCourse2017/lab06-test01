import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2)
        weekday = calculate(2017, 6, 26)
        self.assertEqual(weekday, 0)
        weekday = calculate(1000, 6, 6)
        self.assertEqual(weekday, 3)
        weekday = calculate(-2001, 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(2001, -1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(2001, 1, -3)
        self.assertEqual(weekday, None)
        weekday = calculate(-1, 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(-2001, 1, -3)
        self.assertEqual(weekday, None)
        weekday = calculate(-2001, 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate([35, 7], 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(3, [35, 7], 3)
        self.assertEqual(weekday, None)
        weekday = calculate([35, 7], 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(3, 5, [35, 7])
        self.assertEqual(weekday, None)
        weekday = calculate((35,), 1, 3)
        self.assertEqual(weekday, None)
        weekday = calculate(3, (35,), [35, 7])
        self.assertEqual(weekday, None)


if __name__ == '__main__':
    unittest.main()
