#!/usr/bin/python3
"""
This module creates a Rectangle class.
"""


class Rectangle:
    """
    Rectangles contain ints width and height,
    calculates ints area and perimeter,
    and are printed with '#'.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with int width and/or height.
        """
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        returns self's width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        assigns int value to self's width.
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns self's height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        assigns int value to self's height.
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns self's area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns self's perimeter.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        returns the Rectangle in string form using '#'.
        """
        str_rect = ''
        if self.width > 0 and self.height > 0:
            for i in range(self.height):
                for j in range(self.width):
                    str_rect += '#'
                if i != self.height - 1:
                    str_rect += '\n'
        return str_rect

    def __repr__(self):
        """
        returns a string to recreate the Rectangle in a new instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
