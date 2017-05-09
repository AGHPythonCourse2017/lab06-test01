import sys
import argparse

import unittest

def calculate(year, month, day):
    if year < 0 or month < 0 or day < 0:
        return None
    elif year == 2017:
        return year

    return year + month + day




def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',
                        type=int,
                        required=True,
                        help='Year')
    parser.add_argument('--month',
                        type=int,
                        required=True,
                        help='Month')
    parser.add_argument('--day',
                        type=int,
                        required=True,
                        help='Day')
    parsed_args = parser.parse_args(args)
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    print("Weekday {}".format(weekday))
    return weekday


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
