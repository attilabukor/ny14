#!/usr/bin/env python

import sys, fileinput

def main(args):
    lhs = []
    rhs = []
    for line in fileinput.input(args):
        l = line.split()
        lhs.append(int(l[0]))
        rhs.append(int(l[1]))
    print(countdiffs(lhs, rhs))

def countdiffs(lhs, rhs):
    lhs.sort()
    rhs.sort()
    assert (len(lhs) == len(rhs))

    sumdiff = 0
    for i in range(0, len(lhs)):
        sumdiff += abs(lhs[i] - rhs[i])

    return sumdiff

main(sys.argv[1:])
