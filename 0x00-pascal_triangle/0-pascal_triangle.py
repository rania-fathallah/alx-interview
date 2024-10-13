#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's Triangle.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate. Must be
             a positive integer.

    Returns:
    list: A list of lists, where each inner list represents a row of
           Pascal's Triangle.
    """
    
    array = []
    
    if n <= 0:
        return array
    
    for i in range(1, n + 1):
        arr1 = []
        
        for j in range(i):
            if i == 1 or j == 0 or j == i - 1:
                arr1.append(1)
            else:
                arr1.append(array[i - 2][j - 1] + array[i - 2][j])
        
        array.append(arr1)
    
    return array
