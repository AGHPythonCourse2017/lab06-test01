import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        wrong_date_message = "Wrong date!!!"

        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 2)

        retcode = main(("--year", "2017", "--month", "05", "--day", "9"))
        self.assertEqual(retcode, 1)

        retcode = main(("--year", "2015", "--month", "5", "--day", "9"))
        self.assertEqual(retcode, 5)

        retcode = main(("--year", "2001", "--month", "2", "--day", "30"))
        self.assertEqual(retcode, wrong_date_message)

        retcode = main(("--year", "2001", "--month", "13", "--day", "30"))
        self.assertEqual(retcode, wrong_date_message)

        retcode = main(("--year", "1", "--month", "1", "--day", "1"))
        self.assertEqual(retcode, 5)


if __name__ == '__main__':
    dummy = TestDummy()
    dummy.test_fun()
    unittest.main()
