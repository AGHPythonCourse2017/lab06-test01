import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):
    def test_calculate(self):
        weekday = calculate(2017, 5, 9)
        self.assertEqual(weekday, 1)

        weekday = calculate(1978, 2, 1)
        self.assertEqual(weekday, 2)

        weekday = calculate(2000, 7, 9)
        self.assertEqual(weekday, 6)

        weekday = calculate(2000, 15, 9)
        self.assertEqual(weekday, -1)

        weekday = calculate(2000, 4, 40)
        self.assertEqual(weekday, -1)

        weekday = calculate(200012, 15, 9)
        self.assertEqual(weekday, -1)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        retcode = main(("--year", "-5", "--month", "10", "--day", "20"))
        self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "2033", "--month", "2", "--day", "29"))
        self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "2033", "--month", "2", "--day", "29"))
        self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "2012", "--month", "13", "--day", "15"))
        self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "2010", "--month", "11", "--day", "31"))
        self.assertNotEqual(retcode, 0)


if __name__ == '__main__':
    unittest.main()
