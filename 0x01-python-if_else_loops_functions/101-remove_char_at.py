#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for index, c in enumerate(str):
        if n != index:
            str1 += c
    return str1
