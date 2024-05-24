#!/usr/bin/python3
"""task 7 module"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = list(sys.argv[1:])
try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
