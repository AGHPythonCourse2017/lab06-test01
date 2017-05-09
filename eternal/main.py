import sys
import argparse
from datetime import date


def calculate(year, month, day):
    """
    Calculates day of the week (0-Monday, 1-Tuesday)
    :param year:
    :param month:
    :param day:
    :return:
    """
    weekday = date(year, month, day).weekday() 
    if year < 100:
        weekday = (weekday - 2) % 7
    return weekday


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
    try:
        weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
        print("Weekday {}".format(weekday))
        return weekday
    except ValueError:
        return "Wrong date!!!" 


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
