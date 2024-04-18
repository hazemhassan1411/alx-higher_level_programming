#!/usr/bin/python3
"""square class"""

class Square:
    """square class"""

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    def area(self):
    
        return  self.__size ** 2
    
    def my_print(self):
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="\n" if x is self.__size -1 and i != x else "")
            print()