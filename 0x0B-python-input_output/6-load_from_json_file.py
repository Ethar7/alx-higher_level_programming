#!/usr/bin/python3
"""this is a module documentation"""


import json


def load_from_json_file(filename):
    """this is func doc"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
