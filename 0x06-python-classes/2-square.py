#!/usr/bin/python3
"""square class"""

class Square:

    def __init__(self, size):

        if isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
