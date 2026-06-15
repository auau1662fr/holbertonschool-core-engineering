#!/usr/bin/env python3
"""Module for Square class with getter and setter"""


class Square:
    """A class that represents a square with getter and setter"""

    def __init__(self, size=0):
        """Initialize Square with size validation"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
