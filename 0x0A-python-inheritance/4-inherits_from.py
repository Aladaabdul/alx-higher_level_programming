#!/usr/bin/python3

"""Function declaration

"""


def inherits_from(obj, a_class):
    """is_kind_of_class defination

    Args:
    obj: object
    a_class: class

    Return: True or False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
