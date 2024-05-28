#!/usr/bin/python3
"""this module contains a function"""


def pascal_triangle(n):
    """function def pascal_triangle(n): that returns a
    list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        row.append(1)
        if len(triangle) == 0:
            triangle.append(row)
        elif len(triangle) == 1:
            row.append(1)
            triangle.append(row)
        else:
            previous = triangle[len(triangle)-1]
            for j in range(len(previous)-1):
                result = previous[j] + previous[j+1]
                row.append(result)
            row.append(1)
            triangle.append(row)
    return triangle
