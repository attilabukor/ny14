#!/usr/bin/env python

import fileinput, re

quadrants = {'tl': 0, 'tr': 0, 'bl': 0, 'br': 0}

width = 11
height = 7
seconds = 100

def predict_location(pos, vel, seconds, width, height):
    for i in range(0, seconds):
        pos = ((pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height)

    return pos

def quadrant(pos, width, height):
    if pos[0] < (width - 1) / 2 and pos[1] < (height - 1) / 2:
        return 'tl'
    if pos[0] > (width - 1) / 2 and pos[1] < (height - 1) / 2:
        return 'tr'
    if pos[0] < (width - 1) / 2 and pos[1] > (height - 1) / 2:
        return 'bl'
    if pos[0] > (width - 1) / 2 and pos[1] > (height - 1) / 2:
        return 'br'

    return None

for line in fileinput.input():
    if fileinput.isstdin():
        width = 101
        height = 103
    else:
        width = 11
        height = 7

    m = re.findall("(-?\d+)", line)
    pos = (int(m[0]), int(m[1]))
    vel = (int(m[2]), int(m[3]))

    pos = predict_location(pos, vel, 100, width, height)
    q = quadrant(pos, width, height)
    if q != None:
        quadrants[q] += 1

print(quadrants)
print(quadrants['tl'] * quadrants['tr'] * quadrants['bl'] * quadrants['br'])
