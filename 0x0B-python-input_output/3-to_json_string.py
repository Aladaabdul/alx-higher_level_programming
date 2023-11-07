#!/usr/bin/python3
""" Function defination """
import json


def to_json_string(my_obj):
    """To_json_string function

    Args:
    my_obj: Object

    Return: Json object
    """
    return json.dumps(my_obj)
