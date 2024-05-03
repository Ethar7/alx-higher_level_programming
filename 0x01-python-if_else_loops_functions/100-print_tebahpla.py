#!/usr/bin/python3
for i in range(27):
    c = i + ord('z')
    if i % 2 != 0:
        c += 32
    print("{:c}".format(c), end="")
