#!/usr/bin/python3
"""this is a module documentation"""


def save_to_json_file(my_obj, filename):
    """this is func doc"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
