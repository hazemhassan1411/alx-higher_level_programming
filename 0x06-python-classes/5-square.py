#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """square class"""
        self.__size = size

    @property
    def size(self):
        """square class"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """square class"""
        return self.__size ** 2

    def my_print(self):
        """square class"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="\n" if j is self.__size - 1 and i != j else "")
            print()
