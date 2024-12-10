#!/usr/bin/env python

import fileinput, sys

def draw(matrix):
    for l in matrix:
        for c in l:
            if c == None:
                print(".", end="")
            else:
                print(c, end="")
        print()

def walk(matrix, start, found_peaks, rating=False, prev=None):
    x = start[0]
    y = start[1]
    start_val = matrix[x][y]
    if start_val == 9:
        if rating:
            return 1
        elif start in found_peaks:
            return 0
        else:
            found_peaks.append(start)
            return 1


    sum = 0

    if x > 0 and matrix[x-1][y] == start_val + 1 and prev != (x-1,y):
        sum += walk(matrix, (x-1,y), found_peaks, rating, start)
    if x + 1< len(matrix) and matrix[x+1][y] == start_val + 1 and prev != (x+1,y):
        sum += walk(matrix, (x+1,y), found_peaks, rating, start)
    if y > 0 and matrix[x][y-1] == start_val + 1 and prev != (x,y-1):
        sum += walk(matrix, (x,y-1), found_peaks, rating, start)
    if y + 1 < len(matrix) and matrix[x][y+1] == start_val + 1 and prev != (x,y+1):
        sum += walk(matrix, (x,y+1), found_peaks, rating, start)

    return sum

island = []
trailheads = []
peaks = []
for i, l in enumerate(fileinput.input()):
    line = []
    for j, c in enumerate(l.strip()):
        if c == '.':
            c = None
        else:
            c = int(c)
        line.append(c)
        if c == 0:
            trailheads.append((i,j))
        elif c == 9:
            peaks.append((i,j))
    island.append(line)

sum = 0
for t in trailheads:
    score = walk(island, t, [], False)
    sum += score

print(sum)


sum = 0
for t in trailheads:
    score = walk(island, t, [], True)
    sum += score

print(sum)
