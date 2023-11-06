#!/usr/bin/python3
"""Rectangle class defination"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle class defination

    Args:
    width: Int
    height: Int

    Return: None
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size))
