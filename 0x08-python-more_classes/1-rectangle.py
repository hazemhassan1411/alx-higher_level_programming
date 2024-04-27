#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """square class"""
        self.width = width
        self.hight = height

    @property
    def width(self):
        """square class"""
        return self.__width

    @width.setter
    def width(self, value):
        """square class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """square class"""
        return self.__height

    @height.setter
    def height(self, value):
        """square class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
