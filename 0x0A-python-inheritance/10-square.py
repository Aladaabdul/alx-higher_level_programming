#!/usr/bin/python3
"""Class defination"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherit Rectangle

    Args:
    size: Int

    Return: None
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
