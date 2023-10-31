#!/usr/bin/python3
class LockedClass:
    """ Defination of LockedClass

    Attributes:
    first_name: String

    Return: first_name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Class Initialization

        Args:
        FisrtName: string

        Return: None
        """
        self.first_name = "first_name"
