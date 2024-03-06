#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0
    # Check if most significant bit from the left is set
    mask1 = 1 << 7
    # Check if 2nd most significant bit from the left is set
    mask2 = 1 << 6
    for num in data:
        # Check MSB of each byte
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                # Move to the next bit to the right
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & mask1) and not (num & mask2):
                return False
            num_bytes -= 1
    return num_bytes == 0
