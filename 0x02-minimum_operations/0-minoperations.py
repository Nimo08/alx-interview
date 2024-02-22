#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file
Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    num_op = 0
    num = 2
    while num <= n:
        while n % num == 0:
            num_op += num
            n //= num
        num += 1
    return num_op
