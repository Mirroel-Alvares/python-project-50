import argparse


def cli_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0')
    parser.add_argument(
        '-f', '--format',
        metavar='[type]',
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help='output format (default: "stylish")'
    )

    args = parser.parse_args()
    print(args.first_file, args.second_file)

    return args.first_file, args.second_file
