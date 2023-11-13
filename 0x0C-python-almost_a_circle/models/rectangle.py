#!/usr/bin/python3
"""Class defination

"""
from models.base import Base
import json



class Rectangle(Base):
    """Rectangle class inherit Base class

    Attributes:
    width
    height
    x
    y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Initialization

        Args:
        width
        height
        x
        y

        Return: None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for x

        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x

        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for y

        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y

        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Area function

        Args:
        width
        height

        Return: None
        """
        return self.__width * self.__height

    def display(self):
        """Display function

        Args:
        width
        height

        Return: None
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})\
 {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update function

        Args:
        args: Argument
        kwargs: Keyword args

        Return: None
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int:
                        raise TypeError("value must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """To dictionary function

        """
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }
