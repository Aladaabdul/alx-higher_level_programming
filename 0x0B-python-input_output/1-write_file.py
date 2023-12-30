#!/usr/bin/python3
"""Read File defination"""


def write_file(filename="", text=""):
    """Read_file function

    Args:
    filename: File

    Return: None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
