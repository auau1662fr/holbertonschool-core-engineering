#!/usr/bin/env python3
"""Module for Dragon class with mixins"""


class SwimMixin:
    """A mixin that provides swimming behavior"""

    def swim(self):
        """Print swimming message"""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying behavior"""

    def fly(self):
        """Print flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that represents a dragon"""

    def roar(self):
        """Print roaring message"""
        print("The dragon roars!")
