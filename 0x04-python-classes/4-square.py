#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
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
    def my_print(self):
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end='')
            print()
