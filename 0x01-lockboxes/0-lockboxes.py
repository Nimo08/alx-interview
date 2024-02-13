#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    for key in range(1, len(boxes)):
        boxFlag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                boxFlag = True
                break
        if not boxFlag:
            return False
    return True
