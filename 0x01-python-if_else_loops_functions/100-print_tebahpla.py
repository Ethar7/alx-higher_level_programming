#!/usr/bin/python3
for i in range(25, -1, -1):
    c = i + ord('a')
    if i % 2 == 0:
        c -= 32
    print("{:c}".format(c), end="")
