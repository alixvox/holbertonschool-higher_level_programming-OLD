#!/usr/bin/python3
"""
This module contains class Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is based on Rectanlge from
    the module 9-rectangle.py:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def __init__(self, size):
        """This method instantiates with size:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        if self.integer_validator("size", size):
            self.__width = size
            self.__height = size
            self.__size = size

    def area(self):
        """This method returns area with size:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        return self.__size * self.__size
