#!/usr/bin/python3
"""Base class defination

"""
import json
import csv


class Base:
    """Class Base defination

    Attributes:
    nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Initialization

        Args:
        id

        Return: None
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_objs):
        """Returning json string representation of list of dictionaries"""
        if list_objs is None or list_objs == []:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving list of objects to file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = Base.to_json_string(list_objs)
                f.write(json_string)
