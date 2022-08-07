"""A module containing various custom generators."""


def upper_letters():
    """A range generator for upper case letters."""
    for i in range(ord('A'), ord('Z') + 1):
        yield chr(i)


def lower_letters():
    """A range generator for lower case letters."""
    for i in range(ord('a'), ord('z') + 1):
        yield chr(i)
