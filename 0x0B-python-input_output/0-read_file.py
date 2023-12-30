#!/usr/bin/python3
"""Read File defination"""


def read_file(filename=""):
    """Read_file function

    Args:
    filename: File

    Return: None
    """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
