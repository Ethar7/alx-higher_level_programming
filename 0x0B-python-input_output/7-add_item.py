#!/usr/bin/python3
"""this is module doc"""


import sys
load_from_json_file = _import_('6-load_from_json_file').load_from_json_file
save_to_json_file = _import_('5-save_to_json_file').save_to_json_file


    filename = "add_item.json"
    args = sys.argv[1:]  # Exclude the script name from the arguments

    # Load existing data or create an empty list
    my_list = load_from_json_file(filename)

    # Add command-line arguments to the list
    my_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)                                                                                                                                                  
