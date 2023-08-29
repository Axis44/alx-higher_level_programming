#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """to initialize a new square.size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position tuple if 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current area of the square if success."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
