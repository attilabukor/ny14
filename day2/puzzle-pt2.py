#!/usr/bin/env python

import sys, fileinput

def is_safe_increase(n, nprev):
    return abs(n - nprev) <= 3

def is_report_safe(n, nprev):
    if n > nprev:
        if is_safe_increase(n, nprev):
            return 1
    elif n < nprev:
        if is_safe_increase(n, nprev):
            return -1
    return 0

def main(args):
    safe_reports = 0
    for l in fileinput.input(args):
        nprev = -1
        count = 0
        report = []
        for ns in l.split():
            n = int(ns)
            report.append(n)
            if nprev == -1:
                nprev = n
                continue
            count += is_report_safe(n, nprev)
            nprev = n
        if abs(count) + 1 == len(report):
            safe_reports += 1
        else:
            for remove in range(0, len(report)):
                nprev = -1
                count = 0
                for i in range(0, len(report)):
                    n = report[i]
                    if i == remove:
                        continue
                    if nprev == -1:
                        nprev = n
                        continue
                    count += is_report_safe(n, nprev)
                    nprev = n
                if abs(count) + 2 == len(report):
                    safe_reports += 1
                    break

    print(safe_reports)

main(sys.argv[1:])
