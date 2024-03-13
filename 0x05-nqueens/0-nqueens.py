#!/usr/bin/python3


import sys


def nQueens(N):
    cols = set()
    posDiagonals = set()
    negDiagonals = set()

    board = []

    def backtrack(rows):
        if rows == N:
            print(board)
            return

        for c in range(N):
            if c in cols or (rows + c) in posDiagonals \
                    or (rows - c) in negDiagonals:
                continue

            cols.add(c)
            posDiagonals.add(rows + c)
            negDiagonals.add(rows - c)
            board.append([rows, c])

            backtrack(rows + 1)

            cols.remove(c)
            posDiagonals.remove(rows + c)
            negDiagonals.remove(rows - c)
            board.remove([rows, c])

    backtrack(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
nQueens(int(sys.argv[1]))
