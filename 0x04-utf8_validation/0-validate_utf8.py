#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if num >> 3 == 0b11110:
                num_bytes = 3
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 7 != 0:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
