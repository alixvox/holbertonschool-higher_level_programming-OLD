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
        Initializations of private ints width, height, x, y,
        and optional id.
        """

        self.attribute_checker("width", width)
        self.__width = width
        self.attribute_checker("height", height)
        self.__height = height
        self.attribute_checker("x", x)
        self.__x = x
        self.attribute_checker("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        returns self's width.
        """
        return self.__width

    @property
    def height(self):
        """
        returns self's height.
        """
        return self.__height

    @property
    def x(self):
        """
        returns self's x.
        """
        return self.__x

    @property
    def y(self):
        """
        returns self's y.
        """
        return self.__y

    @x.setter
    def x(self, value):
        """
        assigns int value to self's x.
        """
        self.attribute_checker("x", value)
        self.__x = value

    @width.setter
    def width(self, value):
        """
        assigns int value to self's width.
        """
        self.attribute_checker("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """
        assigns int value to self's height.
        """
        self.attribute_checker("height", value)
        self.__height = value

    @y.setter
    def y(self, value):
        """
        assigns int value to self's y.
        """
        self.attribute_checker("y", value)
        self.__y = value

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

    def area(self):
        """
        returns self's area (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """
        prints self using '#', using x and y.
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        returns a string representation of self in the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}\
".format(self.id, self.__x,
         self.__y, self.__width,
         self.__height)

    def update(self, *args, **kwargs):
        """
        Updates self's attributes with a list of arguments *args,
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary of the attributes of Rectangle
        """
        return {"id": self.id, "width": self.width, "height\
        ": self.height, "x": self.x, "y": self.y}
