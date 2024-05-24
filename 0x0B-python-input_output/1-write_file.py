#!/usr/bin/python3
"""this is a module documentation"""


def write_file(filename="", text=""):
    """this is func doc"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
