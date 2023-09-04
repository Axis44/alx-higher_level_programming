#!/usr/bin/python3
""" Defines Rectangle Module """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize a class """
        self.width = width
        self.height = height

    # returns string representation of the object
    def __str__(self):
        """ string conversion """
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]

    # function that returns the object representation
    def __repr__(self):
        """ string to conversion """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ method is a known as a destructor """
        print("Bye rectangle...")

    @property
    def width(self):
        """ width to getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height to getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of th rectangle clas """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
