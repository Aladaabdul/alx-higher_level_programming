#!/usr/bin/python3
class LockedClass:
    """ Defination of LockedClass

    Attributes:
    first_name: String

    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Class Initialization"""

        self.first_name = "first_name"
