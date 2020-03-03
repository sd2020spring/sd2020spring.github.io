"""
Generate a random binary tree and pirnt the number of nodes in it.

Create a random binary tree whose leaves are all guaranteed to be between a
given minimum and maximum depth. Then go through this list to compute the
number of nodes and print this number to standard output.
"""
import argparse
import random
import sys


# Set the minimum and maximum possible values in the generated tree.
RAND_MIN = 0
RAND_MAX = 100

# Define key names for the tree (which we represent as a dict).
VALUE = "value"
LEFT_SUBTREE = "left"
RIGHT_SUBTREE = "right"


def _build_tree_helper(max_depth):
    if random.randint(0, 1) == 1:
        return build_tree(0, max_depth - 1)
    else:
        return build_tree(0, 0)


def build_tree(min_depth, max_depth):
    """
    Make a random binary tree with a given range of depth.

    Args:
        min_depth: the minimum depth of the tree.
        max_depth: the maximum depth of the tree.

    Returns:
        A nested dict representing the generated tree.
    """
    tree = {VALUE: None}
    if max_depth == 0:
        return tree
    tree[VALUE] = random.randint(RAND_MIN, RAND_MAX)
    if min_depth == 0:
        tree[LEFT_SUBTREE] = _build_tree_helper(max_depth)
        tree[RIGHT_SUBTREE] = _build_tree_helper(max_depth)
    else:
        tree[LEFT_SUBTREE] = build_tree(min_depth - 1, max_depth - 1)
        tree[RIGHT_SUBTREE] = build_tree(min_depth - 1, max_depth - 1)
    return tree


def count_nodes(tree):
    """
    Return the number of nodes in a tree with a value.

    Args:
        tree: A nested dict representing the tree.

    Returns:
        An int representing the number of nodes in the tree.
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
    parser.add_argument("min_depth", type=positive_int,
                        help="Minimum depth of tree")
    parser.add_argument("max_depth", type=positive_int,
                        help="Maximum depth of tree")
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
    random.seed(parsed_args.seed)
    tree = build_tree(parsed_args.min_depth, parsed_args.max_depth)
    print(count_nodes(tree))


if __name__ == '__main__':
    main()
