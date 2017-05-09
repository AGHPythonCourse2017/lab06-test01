import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        weekday1 = calculate(2017, 1, 1)
        self.assertEqual(weekday1, 2017)

        retcode1 = main(("--year", "2017", "--month", "1", "--day", "1"))
        self.assertEqual(retcode, 6)

        weekaday2 = calculate(2017, 1, -10)
        self.assertEqual(weekaday2, None)

        retcode3 = main(("--y", "2017", "--month", "1", "--day", "1"))
        self.assertEqual(retcode3, None)

        retcode4 = main(("--year", "2017", "--m", "1", "--day", "1"))
        self.assertEqual(retcode4, None)




if __name__ == '__main__':
    unittest.main()
