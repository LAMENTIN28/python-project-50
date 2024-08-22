#!/usr/bin/env python3

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                     'files and shows a difference.')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', default='store_const', help='')
    parser.add_argument("--format", "-f", help='set format of output')
    args = parser.parse_args(['first_file', 'second_file'])
    parser.print_help()


if __name__ == '__main__':
    main()
