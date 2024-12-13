#!/usr/bin/env python

import fileinput, re

class Claw:
    button_a: tuple
    button_b: tuple
    prize: tuple

    def __repr__(self):
        return ("Button A: " + self.button_a.__repr__() + ", Button B: "
                + self.button_b.__repr__() + ", Prize: "
                + self.prize.__repr__())

    def check(self):
        x = 0
        y = 0
        m = None
        for a in range(0, 100):
            for b in range(0, 100):
                x = a * c.button_a[0] + b * c.button_b[0]
                y = a * c.button_a[1] + b * c.button_b[1]
                if x == c.prize[0] and y == c.prize[1]:
                    if m == None:
                        m = a * 3 + b
                    else:
                        m = min(m, a * 3 + b)
                elif x > c.prize[0] or y > c.prize[1]:
                    break
        return m

claws = []
claw = Claw()
for l in fileinput.input():
    m = re.findall("Button A: X\+([0-9]+), Y\+([0-9]+)", l)
    if len(m) > 0:
        claw.button_a = (int(m[0][0]), int(m[0][1]))
        continue
    m = re.findall("Button B: X\+([0-9]+), Y\+([0-9]+)", l)
    if len(m) > 0:
        claw.button_b = (int(m[0][0]), int(m[0][1]))
        continue
    m = re.findall("Prize: X=([0-9]+), Y=([0-9]+)", l)
    if len(m) > 0:
        claw.prize = (int(m[0][0]), int(m[0][1]))
        continue

    claws.append(claw)
    claw = Claw()
claws.append(claw)

s = 0
for c in claws:
    price = c.check()
    if price != None:
        #print(">", c, price)
        s += price
    #else:
        #print(c)

print(s)
