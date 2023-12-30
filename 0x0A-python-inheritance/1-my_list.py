#!/usr/bin/python3
"""MyList class defination"""


class MyList(list):
    """MyList defination

    Attributes:
    int: Attributes
    """
    def print_sorted(self):
        """Defination of print_sorted function

        Args:
        list: sorted list

        Return: Sorted list
        """
        print(sorted(self))
