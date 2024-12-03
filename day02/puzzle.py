#!/usr/bin/env python

import sys, fileinput

def main(args):
    safe_reports = 0
    for l in fileinput.input(args):
        prev = -1
        inc = False
        dec = False
        safe = True
        for ns in l.split():
            n = int(ns)
            if prev == -1:
                prev = n
                continue
            if n == prev:
                safe = False
                break
            if n > prev:
                if dec:
                    safe = False
                    break
                inc = True
                if n - prev > 3:
                    safe = False
                    break
            elif n < prev:
                if inc:
                    safe = False
                    break
                dec = True
                if prev - n > 3:
                    safe = False
                    break
            prev = n
        if safe:
            safe_reports += 1
    print(safe_reports)

main(sys.argv[1:])
