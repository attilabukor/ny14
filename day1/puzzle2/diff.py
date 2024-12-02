#!/usr/bin/env python

import sys, fileinput

def main(args):
    lhs = []
    rdict = {}
    for line in fileinput.input(args):
        l = line.split()
        lhs.append(int(l[0]))
        rhs = int(l[1])
        match = rdict.get(rhs)
        if match := rdict.get(rhs):
            rdict[rhs] = match + 1
        else:
            rdict[rhs] = 1
    print(sumdiff(lhs, rdict))

def sumdiff(lhs, rhs):
    sum = 0
    for n in lhs:
        if r := rhs.get(n):
            sum += n * r

    return sum

main(sys.argv[1:])
