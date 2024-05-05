#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == [[]]:  # Check if matrix is empty or contains an empty list
        return
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="\n")  # Print the last element with a newline
            else:
                print("{:d}".format(row[i]), end=" ")  # Print other elements with a space
