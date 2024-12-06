#!/usr/bin/env python

import fileinput
from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def check_obstacle(pos, matrix):
    return matrix[pos[0]][pos[1]] == "#"

def turn_right(direction, pos):
    match direction:
        case Direction.NORTH:
            return Direction.EAST, (pos[0] + 1, pos[1])
        case Direction.EAST:
            return Direction.SOUTH, (pos[0], pos[1] - 1)
        case Direction.SOUTH:
            return Direction.WEST, (pos[0] - 1, pos[1])
        case Direction.WEST:
            return Direction.NORTH, (pos[0], pos[1] + 1)

def walk(pos, direction, matrix):
    unique_positions = {pos}
    while True:
        if (pos[0] < 0 or pos[1] < 0 or pos[0] == len(matrix) or pos[1] ==
            len(matrix[0])):
            break

        if check_obstacle(pos, matrix):
            direction, pos = turn_right(direction, pos)
        else:
            unique_positions.add(pos)

        if direction == Direction.NORTH:
            pos = (pos[0] - 1, pos[1])
        elif direction == Direction.EAST:
            pos = (pos[0], pos[1] + 1)
        elif direction == Direction.SOUTH:
            pos = (pos[0] + 1, pos[1])
        elif direction == Direction.WEST:
            pos = (pos[0], pos[1] - 1)

    return unique_positions

matrix = []
pos = ()
direction: Direction
for x, l in enumerate(fileinput.input()):
    row = []
    matrix.append(row)
    for y, c in enumerate(l.strip()):
        row.append(c)
        if c == "^":
            pos = (x,y)
            direction = Direction.NORTH
        elif c == ">":
            pos = (x,y)
            direction = Direction.EAST
        elif c == "v":
            pos = (x,y)
            direction = Direction.SOUTH
        elif c == "<":
            pos = (x,y)
            direction = Direction.WEST


print(len(walk(pos, direction, matrix)))
