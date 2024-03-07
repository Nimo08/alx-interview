#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Use bitwise operators to check through bytes
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    # Define constants for bit masks
    MASK_1_BYTE = 0b10000000
    MASK_2_BYTES = 0b11100000
    MASK_3_BYTES = 0b11110000
    MASK_CONTINUATION = 0b10000000

    num_bytes = 0
    for num in data:
        # Check if num is within valid range
        if num < 0 or num > 255:
            return False
        if num_bytes == 0:
            if num & MASK_1_BYTE == 0:
                continue
            elif num & MASK_3_BYTES == MASK_3_BYTES:
                num_bytes = 3
            elif num & MASK_2_BYTES == MASK_2_BYTES:
                num_bytes = 2
            elif num & MASK_CONTINUATION == MASK_CONTINUATION:
                return False
        else:
            if num & MASK_CONTINUATION != MASK_CONTINUATION:
                return False
            num_bytes -= 1

    return num_bytes == 0
