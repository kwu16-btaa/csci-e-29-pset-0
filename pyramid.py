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
    if (isinstance(rows, int) is False) or (rows <= 0):
        print('Please enter number greater than 0')
        return

    for i in range(1, rows + 1):
        # line to be printed

        # number of dashes on each side
        num_dashes = rows - i

        line = "-" * num_dashes + "=" * (2*i - 1) + "-" * num_dashes

        print(line)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
