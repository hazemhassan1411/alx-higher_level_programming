#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size

    def area(self):

        return self.__size ** 2
