#!/usr/bin/python3
""" Function defination """
import json


def from_json_string(my_str):
    """To_json_string function

    Args:
    my_str: String

    Return: Json object
    """
    return json.loads(my_str)
