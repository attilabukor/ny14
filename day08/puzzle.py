#!/usr/bin/env python

import fileinput, re, itertools

def draw(matrix):
    for row in matrix:
        print(*row)

def check_coordinates(x, y, matrix):
    return x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[x])

matrix = []
antennae = {}
for i, l in enumerate(fileinput.input()):
    row = []
    for m in re.finditer('[0-9a-zA-Z]', l):
        if m.group() not in antennae:
            antennae[m.group()] = []
        antennae[m.group()].append((i, m.span()[0]))
    for c in l.strip():
        row.append(c)
    matrix.append(row)

antinodes = set()

for f in antennae:
    for a in itertools.combinations(antennae[f], 2):
        diff = (a[1][0] - a[0][0], a[1][1] - a[0][1])
        x1 = a[0][0] - diff[0]
        y1 = a[0][1] - diff[1]
        if check_coordinates(x1, y1, matrix):
            matrix[x1][y1] = '#'
            antinodes.add((x1, y1))

        x2 = a[1][0] + diff[0]
        y2 = a[1][1] + diff[1]
        if check_coordinates(x2, y2, matrix):
            matrix[x2][y2] = '#'
            antinodes.add((x2, y2))

#draw(matrix)
print(len(antinodes))
