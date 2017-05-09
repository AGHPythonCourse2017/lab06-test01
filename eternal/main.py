import sys
import argparse
import datetime


def calculate(year, month, day):
    """
    Calculates day of the week (0-Monday, 1-Tuesday)
    :param year:
    :param month:
    :param day:
    :return:
    """
    try:
        data1 = datetime.date(year, month, day).weekday()
        return data1
    except ValueError:
        return -1


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
    if parsed_args.year < 0 or parsed_args.day < 0 or parsed_args.month <0:
        return -1
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    if weekday < 0:
        return -1
    print("Weekday {}".format(weekday))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
