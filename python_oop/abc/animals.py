#!/usr/bin/env python3
"""Module for abstract Animal class and subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal"""
        pass


class Dog(Animal):
    """A class that represents a dog"""

    def sound(self):
        """Return the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """A class that represents a cat"""

    def sound(self):
        """Return the sound of a cat"""
        return "Meow"
