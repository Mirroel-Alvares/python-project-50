#!usr/bin/env python3

from gendiff.cli import cli_parser
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file = cli_parser()
    print(generate_diff(first_file,
                        second_file)
          )


if __name__ == '__main__':
    main()
