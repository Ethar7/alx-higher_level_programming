#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    
    def is_first_occurrence(x):
        if x not in seen:
            seen.add(x)
            return True
        return False
    unique_elements = filter(is_first_occurrence, my_list)
    return sum(unique_elements)
