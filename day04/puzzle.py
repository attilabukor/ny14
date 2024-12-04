#!/usr/bin/env python

import fileinput, sys, re

def part1(matrix):
    count = 0
    w = len(matrix[0])
    h = len(matrix)

    for r in range(0, h):
        for c in range(0, w):
            if matrix[r][c] != "X":
                continue

            if c < w - 3:
                if (matrix[r][c+1] == "M" and matrix[r][c+2] == "A" and
                    matrix[r][c+3] == "S"):
                    count += 1
            if c >= 3:
                if (matrix[r][c-1] == "M" and matrix[r][c-2] == "A" and
                    matrix[r][c-3] == "S"):
                    count += 1
            if r < h - 3:
                if (matrix[r+1][c] == "M" and matrix[r+2][c] == "A" and
                    matrix[r+3][c] == "S"):
                    count += 1
            if r >= 3:
                if (matrix[r-1][c] == "M" and matrix[r-2][c] == "A" and
                    matrix[r-3][c] == "S"):
                    count += 1
            if c < w - 3 and r < h - 3:
                if (matrix[r+1][c+1] == "M" and matrix[r+2][c+2] == "A" and
                    matrix[r+3][c+3] == "S"):
                    count += 1
            if c >= 3 and r >= 3:
                if (matrix[r-1][c-1] == "M" and matrix[r-2][c-2] == "A" and
                    matrix[r-3][c-3] == "S"):
                    count += 1
            if c < w - 3 and r >= 3:
                if (matrix[r-1][c+1] == "M" and matrix[r-2][c+2] == "A" and
                    matrix[r-3][c+3] == "S"):
                    count += 1
            if c >= 3 and r < w - 3:
                if (matrix[r+1][c-1] == "M" and matrix[r+2][c-2] == "A" and
                    matrix[r+3][c-3] == "S"):
                    count += 1

    return count

matrix = []
for l in fileinput.input(sys.argv[1:]):
    row = []
    for c in l:
        if c != "\n":
            row.append(c)
    matrix.append(row)

print(part1(matrix))
