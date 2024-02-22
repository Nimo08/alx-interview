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
    if not isinstance(n, int):
        return 0
    num_op = 0
    # start from 2 'H's
    for num in range(2, n + 1):
        # check if num is a factor of n
        while n % num == 0:
            # add number of smaller problems to result
            num_op += num
            # create smaller problem: move closer to n == 1
            n //= num
    return num_op
