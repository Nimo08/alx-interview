#!/usr/bin/python3
"""
Contains functions to print Pascal's triangle.
"""


def factorial(x):
    """
    Computes factorial of a number.
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    result = []
    if n <= 0:
        return result
    for i in range(n):
        row = []
        for j in range(i + 1):
            ans = factorial(i) // (factorial(j) * factorial(i-j))
            row.append(ans)
        result.append(row)
    return result
