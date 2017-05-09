import sys
import argparse

def calculate(year, month, day):
    """
    Calculates day of the week (0-Monday, 1-Tuesday)
    :param year:
    :param month:
    :param day:
    :return:
    """

    wrong_date_message = "Wrong date!!!"

    if month < 3:
        z = year - 1
        c = 0
    else:
        z = year
        c =2

    if month > 13:
        return wrong_date_message
    if month == 2:
        if year % 4 == 0:
            if day > 29:
                return wrong_date_message
        elif day > 28:
            return wrong_date_message
        
    weekday = ((23*month/9.0) + day + 4 + year + z/4.0 + z/100.0 + z/400.0 - c) % 7

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
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)

    print("Weekday {}".format(weekday))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
