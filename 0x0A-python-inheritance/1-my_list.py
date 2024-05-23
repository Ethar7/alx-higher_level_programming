#!/usr/bin/python3
"""this is the module documentation"""


class MyList(list):
    """my list class"""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
