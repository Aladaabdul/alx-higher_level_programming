#!/usr/bin/python3
"""Rectangle class defination"""


class Rectangle:
    """Rectangle class

    Attributes:
    __width(int): Width of the rectangle
    __height(int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize Rectangle class

        Args:
        width(int): width
        height(int): height

        Return: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrive width

        Args:
        width: Int

        Return: None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
        width: Int

        Return: None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property to retrive height

        Args:
        height: Int

        Return: None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
        height: Int

        Return: None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
