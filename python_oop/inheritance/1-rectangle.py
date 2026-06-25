#!/usr/bin/env python3
"""Module for Rectangle class"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
