import unittest
import random

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 12, 31)
        self.assertEqual(weekday, 0)
        weekday = calculate(-1, 12, 31)
        self.assertEqual(weekday, None) # Przepraszam jesli nie tak, no ale jest swietny wyjatek
        weekday = calculate(random.randint(2000, 2017),
                            random.randint(1, 12),
                            random.randint(1, 28))
        self.assertIn(weekday, [i for i in range(0, 7)])


        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)


if __name__ == '__main__':
    unittest.main()
