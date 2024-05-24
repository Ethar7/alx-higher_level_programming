#!/usr/bin/python3
"""task 7 module"""


import sys
save_to_json_file =  __import__('6-load_from_json_file').load_from_json_file
load_from_json_file __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = list(sys.argv[1:])  # Exclude the script name from the arguments
try:
    # Load existing data or create an empty list
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []
# Add command-line arguments to the list
my_list.extend(args)
 # Save the updated list to the file
save_to_json_file(my_list, filename)
