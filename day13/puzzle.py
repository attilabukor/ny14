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
        a = self.button_a[0]
        a2 = self.button_a[1]
        b = self.button_b[0]
        b2 = self.button_b[1]
        c = self.prize[0]
        c2 = self.prize[1]
        det = a * b2 - b * a2

        assert det != 0, "Determinant is 0, which is not yet handled"

        x = (c * b2 - b * c2) / det
        y = (a * c2 - c * a2) / det
        if x % 1 == 0 and y % 1 == 0:
            return int(x) * 3 + int(y)
        else:
            return None


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
s2 = 0
for c in claws:
    price = c.check()
    if price != None:
        #print(">", c, price)
        s += price
    #else:
        #print(c)

    c2 = c
    c2.prize = (c2.prize[0] + 10000000000000, c2.prize[1] + 10000000000000)
    price = c2.check()
    if price != None:
        s2 += price
        #print(">", c, price)
    #else:
        #print(c)

print(s)
print(s2)
