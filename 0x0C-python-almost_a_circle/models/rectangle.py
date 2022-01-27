#!/usr/bin/python3
"""
This module contains a class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangles inherit from Base and are defined
    by  ints width and height,
    and private ints x and y. They also have
    optional public int id.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiaizations of private ints width, height, x, y,
        and optional id.
        """

        print("{}: x".format(x))
        self.attribute_checker("width", width)
        self.attribute_checker("height", height)
        self.attribute_checker("x", x)
        self.attribute_checker("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        print("{}: __x".format(self.__x))
        self.__y = y
        if id is not None:
            super().__init__(id)

    def attribute_checker(self, attr, value):
        """
        Checks that width and height are greater than 0.
        """
        if attr == 'width' or attr == 'height':
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(attr))
            elif value <= 0:
                raise ValueError("{} must be > 0".format(attr))
        else:
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(attr))
            elif value < 0:
                raise ValueError("{} must be >= 0".format(attr))


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
        self.attribute_checker("width", value)
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
        self.attribute_checker("height", height)
        self.__height = value

    @property
    def x(self):
        """
        returns self's x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        assigns int value to self's x.
        """
        self.attribute_checker("x", x)
        self.__x = value

    @property
    def y(self):
        """
        returns self's y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        assigns int value to self's y.
        """
        self.attribute_checker("y", y)
        self.__y = value
