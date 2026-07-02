#!/usr/bin/env python3
"""Module for Shape abstract class and subclasses"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Abstract method that returns the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that returns the perimeter of the shape"""
        pass


class Circle(Shape):
    """A class that represents a circle"""

    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class that represents a rectangle"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
