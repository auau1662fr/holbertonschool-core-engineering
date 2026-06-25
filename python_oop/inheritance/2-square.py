#!/usr/bin/env python3
"""Module for Square class with __str__"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square"""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
