#!/usr/bin/python3
"""This is a module for adding command-line arguments to a list and saving it as JSON."""

import sys
from _import_('6-load_from_json_file').load_from_json_file
from _import_('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
args = list(sys.argv[1:])  # Exclude the script name from the arguments
try:
    # Load existing data or create an empty list
    my_list = load_from_json_file(filename)
except:
    my_list = []
# Add command-line arguments to the list
my_list.extend(args)
 # Save the updated list to the file
save_to_json_file(my_list, filename)
