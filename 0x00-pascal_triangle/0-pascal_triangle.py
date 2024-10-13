#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's Triangle.

    Pascal's Triangle is a triangular array where each entry is the sum of the
    two entries directly above it. It starts with a single '1' at the top.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists, where each inner list represents a row of
          Pascal's Triangle. If n <= 0, returns an empty list.

    Example:
    >>> pascal_triangle(5)
    [[1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1]]
    """
    array = []

    if n <= 0:
        return array

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(array[i - 1][j - 1] + array[i - 1][j])
        array.append(row)

    return array
