#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """square class"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.height == 0 or self.__width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n")
                * self.height)[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + "," + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
