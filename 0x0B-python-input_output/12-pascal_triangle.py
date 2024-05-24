#!/usr/bin/python3
"""this is module documentation"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            # Calculate nCr using factorials
            value = 1
            for k in range(j):
                value *= (i - k)
                value //= (k + 1)
            row.append(value)
        triangle.append(row)

    return triangle
