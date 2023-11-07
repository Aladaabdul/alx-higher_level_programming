#!/usr/bin/python3
"""Read File defination"""


def append_write(filename="", text=""):
    """Read_file function

    Args:
    filename: File

    Return: None
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_file = f.write(text)
        return append_file
