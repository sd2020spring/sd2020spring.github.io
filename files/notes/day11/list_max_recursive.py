"""
Build a list of random integers, and calculate and print out the maximum value.

Read a list of integers from standard input. Each line is assumed to be a
single integer. These integers are loaded into a list. Recurse through this
list to find the largest integer in the list, and print it to standard output.
"""
import argparse
import random
import sys


# Set the minimum and maximum possible values in the generated list.
RAND_MIN = -1000000000
RAND_MAX = 1000000000

# This code can end up doing a lot of recursion if the list is long, so
# increase the maximum allowed recursion depth. If your machine runs out of
# memory while executing this script, try reducing this value.
sys.setrecursionlimit(1000000)


def build_list(list_size, rand_seed=None):
    """
    Build a list of integers by reading from standard input.

    Args:
        list_size: the number of integers to include in the list.
        rand_seed: the seed value for the pseudorandom number generator.

    Returns:
        A list representing the sequence of integers read from stdin.
    """
    random.seed(rand_seed)
    return [random.randint(RAND_MIN, RAND_MAX) for _ in range(list_size)]


def list_max(int_list):
    """
    Compute the maximum integer in a list.

    Args:
        int_list: a list of ints to find the maximum value in.

    Returns:
        An int representing the maximum value in int_list.
    """
    pass  # FILL THIS IN


def positive_int(value):
    """
    Parse and integer and return it if it is positive.

    Args:
        value: A value of any type representing a potential positive integer.

    Returns:
        An int representing the integer form of value.

    Raises:
        argparse.ArgumentTypeError if value parses to an int but is not
        positive.
    """
    positive_value = int(value)
    if positive_value <= 0:
        raise argparse.ArgumentTypeError(
            f"{value} is not a positive integer")
    return positive_value


def get_parser(name):
    """
    Create and return the command-line argument parser for this script.

    Args:
        name: A str representing the name of the script (usually the name of
              this file).

    Returns:
        An ArgumentParser to process the command-line arguments for this
        script.
    """
    parser = argparse.ArgumentParser(name)
    parser.add_argument("-s", "--seed", type=int, default=None,
                        help="Seed for the pseudorandom number generator")
    parser.add_argument("list_size", type=positive_int,
                        help="Size of candidate integer list")
    return parser


def main(args=sys.argv):
    """
    Run the main logic of the script.

    Args:
        args: a list of arguments to the script, with the first being the name
              of the script and the remainder being arguments to the script.
    """
    parser = get_parser(args[0])
    parsed_args = parser.parse_args(args[1:])
    int_list = build_list(parsed_args.list_size, parsed_args.seed)
    print(list_max(int_list))


if __name__ == '__main__':
    main()
