#!/usr/bin/python3
"""square class defination"""


class Square:
    """a square defines a square

    Attributes:
    __size(int): size int of the square
    """
    def __init__(self, size=0):
        """initialize a the class square

        Args:
        size(int): variable size

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """a function that return area

        Args:
        size(int): Integer

        Returns: Area
        """
        return self.__size ** 2
