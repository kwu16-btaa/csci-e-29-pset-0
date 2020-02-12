#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    # number of characters to be printed on each line
    num_char = 2 * rows - 1

    for i in range(rows):
        # line to be printed
        line = ""
        # starting position of the pyramid stones
        # starting position of the reverse of row count
        # i.e. the starting position of first row is the largest and starting position of last row is 0
        # e.q. if rows = 3, the starting position of 1st row is 2, for 3rd row, it is 0
        start_pos = rows - i - 1
        num_stones = 2 * (i + 1) - 1
        for j in range(num_char):
            if (j >= start_pos) and (j < start_pos + num_stones):
                line += '='
            else:
                line += '-'
        # print(line, "\n")
        print(line)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
