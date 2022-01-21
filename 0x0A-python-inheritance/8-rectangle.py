#!/usr/bin/python3
"""
This module contains class Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangles inherit from class BaseGeometry and contain positive
    ints width and height.
    """

    def __init__(self, width, height):
        """
        initializes with a positive int width and height.
        """

        if self.integer_validator("width", width):
            self.__width == width
        if self.integer_validator("height", height):
            self.__height == height