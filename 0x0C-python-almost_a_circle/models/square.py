#!/usr/bin/python3
"""
This module contains a class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Squares are Rectangles that have the same width and height,
    and so int size is used in place of width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization with size, x, y, and optional id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        returns square's size (width).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Assigns value to square's width and height.
        """
        super().attribute_checker('width', value)
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns a string representation of self in the format:
        [Sqyare] (<id>) <x>/<y> - <size>.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}\
        ".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates square's attributes with a list of
        arguments *args, and optional **kwargs.
        """
        attrs = ['id', 'size', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
