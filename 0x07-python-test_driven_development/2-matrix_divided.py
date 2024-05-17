#!/usr/bin/python3
""" this is for module documentation"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a divisor.
    The matrix must be a list of lists of integers or floats.
    Each row of the matrix must have the same size.
    The divisor must be a non-zero number (integer or float).
    The result is rounded to 2 decimal places.

    Args:
    matrix: list of lists of integers/floats.
    div: non-zero integer or float.

    Returns:
    A new matrix with the division results.
    """
    if not isinstance(matrix, list) or 
    not all(isinstance(row, list) for row in matrix) 
    or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "main":
    import doctest
    doctest.testfile(tests/2-matrix_divided.txt)
