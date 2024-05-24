#!/usr/bin/python3
"""this is a module documentation"""


def append_write(filename="", text=""):
    """this is func doc"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
