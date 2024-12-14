#!/usr/bin/env python

import fileinput, re
from PIL import Image, ImageColor

quadrants = {'tl': 0, 'tr': 0, 'bl': 0, 'br': 0}

width = 11
height = 7
seconds = 100

class Robot:
    pos = (0, 0)
    vel = (0, 0)

def predict_location(pos, vel, seconds, width, height):
    for i in range(0, seconds):
        pos = step_robot(pos, vel, width, height)

    return pos

def step_robot(pos, vel, width, height):
    return ((pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height)

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

robots = []

fullsize = False
for line in fileinput.input():
    if fileinput.isstdin():
        fullsize = True
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

    r = Robot()
    r.pos=pos
    r.vel=vel
    robots.append(r)

print(quadrants)
print(quadrants['tl'] * quadrants['tr'] * quadrants['bl'] * quadrants['br'])

for s in range(0, width*height):
    img = Image.new('RGB', (width, height),color=(255,255,255))
    for r in robots:
        img.putpixel(r.pos, (35,161,60))
        r.pos=(step_robot(r.pos, r.vel, width, height))
    img.save('renders/' + str(s).zfill(5) + '.jpg')
