#!/usr/bin/python3
"""square class defination"""


class Square:
    """a square defines a square

    Attributes:
    __size(int): size int of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize a the class square

        Args:
        size(int): variable size

        Returns: None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Set property

        Args:
        value(int): int

        Returns: None
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Initianize setters

        Args:
        value(int): Variable int

        Returns: None
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Initialize area

        Args:
        size(int): Int

        Returns: None
        """
        return self.__size ** 2

    def my_print(self):
        """Initialize my_print

        Args:
        size(int): Int

        Returns: None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
