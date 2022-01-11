"""This module creates a class called Square."""
class Square:
    """
    This class creates a Square.
    Attributes:
        __size (int): Size of the square
    """
    def __init__(self, size=0):
        """Intializes a Square with int size greater
        than or equal to zero"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size * self.__size
