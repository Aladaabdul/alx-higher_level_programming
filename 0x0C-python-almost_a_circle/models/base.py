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
    def to_json_string(list_dictionaries):
        """Returning json string representation of list of dictionaries

        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving list of objects to file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returning json list of json string representstion"""
        if json_string is None or json_string == "[]":
            return []
        json.loads(json_string)
