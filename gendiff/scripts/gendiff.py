import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class = argparse.RawTextHelpFormatter
    )
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument(
        '-f', '--format', metavar='[type]', choices=['stylish', 'plain', 'json'], default='stylish',
        help='output format (default: "stylish")'
    )

    args = parser.parse_args()
    print(f'First file: {args.first_file}')
    print(f'Second file: {args.second_file}')
    print(f'Format: {args.format}')


if __name__ == '__main__':
    main()