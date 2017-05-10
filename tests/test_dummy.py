import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def main_test(self):
        testes_value = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(testes_value, 0)  # exit code 0

        tested_value3 = main(("--year", "2017", "--month", "1", "--day", "12"))
        self.assertEqual(tested_value3, 0)

        tested_value3 = main(("--year", "2012", "--month", "12", "--day", "23"))
        self.assertEqual(tested_value3, 0)

        # Not Equals:
        tested_value1 = main(("--years", "2001-2098", "--month", "1 2", "--day", "12"))
        self.assertNotEquals(tested_value1, 0)

        tested_value2 = main(("--year", "2098", "--month", "1 2", "--day", "12"))
        self.assertNotEquals(tested_value2, 0)

        tested_value3 = main(("--year", "2017", "--month", "styczeń", "--day", "12"))
        self.assertNotEquals(tested_value3, 0)

        tested_value3 = main(("--year", "rat Year", "--month", "1", "--day", "12"))
        self.assertNotEquals(tested_value3, 0)

    def test_calculate(self):
        tested_weekday = calculate(2001-2034, 1, 3)
        self.assertEqual(tested_weekday, None)

        tested_weekday = calculate(2017, 1, 0)
        self.assertEqual(tested_weekday, None)

        tested_weekday = calculate(2017, 2, 29)
        self.assertEqual(tested_weekday, None)

        tested_weekday = calculate(2234, 3, 12)
        self.assertEqual(tested_weekday, None)

        tested_weekday = calculate(2101, "II", 23)
        self.assertEqual(tested_weekday, None)

        tested_weekday = calculate(2101, 1, 19)
        self.assertEqual(tested_weekday, 2)

        tested_weekday = calculate(2018, 12, 27)
        self.assertEqual(tested_weekday, 3)

        tested_weekday = calculate(2017, 1, 3)
        self.assertEqual(tested_weekday, 1)

        tested_weekday = calculate("300p.n.e.", 12, 3)
        self.assertEqual(tested_weekday, None)

        # weekday = calculate(2001, 1, 3)
        # self.assertEqual(weekday, 2005)


if __name__ == '__main__':
    unittest.main()
