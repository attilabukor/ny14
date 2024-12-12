#!/usr/bin/env python

import fileinput

def draw(matrix):
    for l in matrix:
        for c in l:
            if c == None:
                print(".", end="")
            else:
                print(c, end="")
        print()

def load():
    matrix = []
    for l in fileinput.input():
        row = []
        for c in l.strip():
            row.append(c)
        matrix.append(row)
    return matrix

def get_region(matrix, starting_point, walked=[]):
    if starting_point in walked:
        return walked

    walked.append(starting_point)

    x = starting_point[0]
    y = starting_point[1]
    n = matrix[x][y]

    if len(matrix) > x + 1 and  matrix[x+1][y] == n:
        get_region(matrix, (x+1,y), walked)
    if len(matrix[x]) > y + 1 and matrix[x][y+1] == n:
        get_region(matrix, (x,y+1), walked)
    if x > 0 and matrix[x-1][y] == n:
        get_region(matrix, (x-1, y), walked)
    if y > 0 and matrix[x][y-1] == n:
        get_region(matrix, (x, y-1), walked)

    return walked

farm = load()
#draw(farm)

def area(region):
    return len(region)

def perimeter(region):
    perimeter = 0
    for p in region:
        x = p[0]
        y = p[1]
        if (x+1,y) not in region:
            perimeter += 1
        if (x-1,y) not in region:
            perimeter += 1
        if (x,y+1) not in region:
            perimeter += 1
        if (x,y-1) not in region:
            perimeter += 1

    return perimeter

def sides(region):
    sides = 0
    for p in region:
        x = p[0]
        y = p[1]

        # Outer corners clockwise from top-left corner
        if (x-1,y) not in region and (x,y-1) not in region:
            sides += 1
        if (x,y-1) not in region and (x+1,y) not in region:
            sides += 1
        if (x+1,y) not in region and (x,y+1) not in region:
            sides += 1
        if (x-1,y) not in region and (x,y+1) not in region:
            sides += 1

        # Inner corners clockwise from top-left corner
        if (x+1,y+1) not in region and (x+1,y) in region and (x,y+1) in region:
            sides += 1
        if (x-1,y-1) not in region and (x-1,y) in region and (x,y-1) in region:
            sides += 1
        if (x-1,y+1) not in region and (x-1,y) in region and (x,y+1) in region:
            sides += 1
        if (x+1,y-1) not in region and (x+1,y) in region and (x,y-1) in region:
            sides += 1

    return sides

all_walked = []
price = 0
disc_price = 0

for x, row in enumerate(farm):
    for y, name in enumerate(row):
        if (x,y) in all_walked:
            continue
        
        region = get_region(farm, (x,y), [])
        #print(name, "area", area(region), "perimeter", perimeter(region))
        #print(name, "area", area(region), "sides", sides(region))
        price += area(region) * perimeter(region)
        disc_price += area(region) * sides(region)
        all_walked.extend(region)

print(price, disc_price)
