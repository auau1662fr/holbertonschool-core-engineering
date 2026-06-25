#!/usr/bin/env python3
"""Module for Square class"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
