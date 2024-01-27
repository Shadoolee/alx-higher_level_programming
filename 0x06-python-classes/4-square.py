#!/usr/bin/python3

"""Define a class Sqaure."""


class Sqaure:
    """Represent a sqaure."""

    def __init__(self, size=0):
        """Initialize a new sqaure.

        Args:
            size (int): The size of the new sqaure.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the sqaure."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the cureent area of the sqaure."""
        return (self.__size * self.__size)
