import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 3)

        weekday2 = calculate(2016, 10, 15)
        self.assertEqual(weekday2, 6)

        weekday3 = calculate(2017, 2, 28)
        self.assertEqual(weekday3, 1)

        weekday4 = calculate(2017, 2, 29)
        self.assertNotEqual(weekday4, 2)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        retcode = main(("--year", "2017", "--month", "2", "--day", "29"))
        self.assertNotEqual(retcode, 0)



if __name__ == '__main__':
    unittest.main()
