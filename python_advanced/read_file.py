#!/usr/bin/env python3
"""Module for reading a file"""


def read_file(filename=""):
    """Read a text file and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
