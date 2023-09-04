#!/usr/bin/python3
""" Defines Rectangle Module """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialize values to width, height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width to getter """
    # Private instance attribute: width:
        return self.__width

    @width.setter
    # property setter
    def width(self, value):
        # width must be integer
        if isinstance(value, int) is False:
            # TypeError exception
            raise TypeError('width must be an integer')
            # if width is less than 0, raise a ValueError exception
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height to getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ width getter """
        # Private instance attribute: height:
        return self.__height

    # property setter
    @height.setter
    def height(self, value):
        """ height setter """
        # height must be an integer
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        # if height is less than 0, raise a ValueError
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    # Public instance method,def area(self),returns the rectangle area
    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    # Public instance method,def perimeter(self) with rectangle perimeter
    def perimeter(self):
        """ returns perimeter of rectangle """
        # if width or height is equal to 0, perimeter is equal to 0
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
