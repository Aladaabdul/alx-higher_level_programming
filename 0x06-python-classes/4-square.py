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
        self.size = size

    @property
    def size(self):
        """Initialize property

        Args:
        size(int): Variable int

        Returns: None
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize Setters

        Args:
        size(int): Variable int

        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """a function that return area

        Args:
        size(int): Integer

        Returns: Area
        """
        return self.__size ** 2
