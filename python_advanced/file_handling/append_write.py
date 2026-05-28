#!/usr/bin/env python3
"""Module for appending to a file"""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
