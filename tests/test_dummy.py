import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        # weekday = calculate(2001, 1, 3)
        # self.assertEqual(weekday, 2005)
        #
        # retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        # self.assertEqual(retcode, 0)

        weekday = calculate(2011, 5, 13)
        self.assertEqual(weekday, 4)

        weekday = calculate(2016, 2, 29)
        self.assertEqual(weekday, 0)

        weekday = calculate(2018, 5, 2)
        self.assertEqual(weekday, 2)

        retcode = main(("--year", "2011", "--month", "5", "--day", "13"))
        self.assertEqual(retcode, 0)


if __name__ == '__main__':
    unittest.main()
