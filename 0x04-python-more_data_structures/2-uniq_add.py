#!/usr/bin/python3
def uniq_add(my_list=[]):
    return map(lambda x, y: x + y if x != y, my_list)
