#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Use bitwise operators to check through bytes
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0

    for byte in data:
        # Check the leading bits which determine the continuation bits
        if num_bytes == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            # If this is already a continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
