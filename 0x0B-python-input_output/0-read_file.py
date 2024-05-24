#!/usr/bin/python3
"""this is module documentation"""


def read_file(filename=""):
    """this is a function open file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
