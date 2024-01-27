#!/usr/bin/python3

"""Define a class Square."""


class Sqaure:
    """Represent a square."""

    def __init__(self, size=0):
        """Intiialize a new Square.

        Args:
            size (int): The size of the new sqaure.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif szie < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
