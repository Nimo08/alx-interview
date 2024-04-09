#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            # Land cell
            if grid[i][j] == 1:
                # Assume all 4 sides are surrounded by water
                perimeter += 4

                # Check adjacent cells
                # Check upper cell
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 because upper and current cell share one side
                    perimeter -= 2
                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtract 2 because left and current cell share one side
                    perimeter -= 2

    return perimeter
