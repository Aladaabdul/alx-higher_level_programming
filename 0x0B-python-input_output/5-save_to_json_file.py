#!/usr/bin/python3
"""Function defination"""
import json


def save_to_json_file(my_obj, filename):
    """Save to json function

    Args:
    my_obj: Object
    filename: File

    Return: None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
