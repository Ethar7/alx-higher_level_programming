#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            print("{:c}".format(ord(c)), end="")
        else:
            print("{:c}".format(ord(c) - 32), end="")
