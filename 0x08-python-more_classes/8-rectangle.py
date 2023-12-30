#!/usr/bin/python3
"""Rectangle class defination"""


class Rectangle:
    """Rectangle class

    Attributes:
    __width(int): Width of the rectangle
    __height(int): Height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle class

        Args:
        width(int): width
        height(int): height

        Return: None
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retrive width

        Args:
        width: Int

        Return: None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
        width: Int

        Return: None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property to retrive height

        Args:
        height: Int

        Return: None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
        height: Int

        Return: None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area instance method

        Args:
        width: Int
        height: Int

        Return: Area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter instance method

        Args:
        width: Int
        height: Int

        Return: Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + "\n"
        return rec_str[:-1]

    def print(self):
        rec_str = str(self)
        if rec_str:
            print(rec_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
