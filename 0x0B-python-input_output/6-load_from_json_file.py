#!/usr/bin/python3
"""Function defination"""
import json


def load_from_json_file(filename):
    """Load from json function

    Args:
    my_obj: Object
    filename: File

    Return: None
    """
    with open(filename) as f:
        return json.load(f)
