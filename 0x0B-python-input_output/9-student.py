#!/usr/bin/python3
"""Student class defination


"""


class Student():
    """Student class

    Attributes:
    first_name: String
    last_name: String
    age: Int

    """
    def __init__(self, first_name, last_name, age):
        """class Initialization

        Args:
        first_name
        last_name
        age

        Returns: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function defination

        """
        return self.__dict__
