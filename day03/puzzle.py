#!/usr/bin/env python

import sys, fileinput, re

def mul(line):
    res = 0
    for m in re.findall("mul\(([0-9]+),([0-9]+)\)", line):
        res += int(m[0]) * int(m[1])

    return res

def part1(args):
    res = 0
    for l in fileinput.input(args):
        res += mul(l)

    return res

def part2(args):
    res = 0
    do = True
    for l in fileinput.input(args):
        for s in re.split("(do(?:n't)?\(\))", l):
            if s == "do()":
                do = True
            elif s == "don't()":
                do = False
            elif do and s != None:
                res += mul(s)

    return res

def main(args):
    print(part2(args))

main(sys.argv[1:])
