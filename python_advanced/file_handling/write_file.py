#!/usr/bin/env python3
"""Module for writing to a file"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
