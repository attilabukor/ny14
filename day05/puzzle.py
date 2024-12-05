#!/usr/bin/env python

import fileinput, itertools, functools

def check_order(order, rules):
    correct = True
    for i, page in enumerate(order):
        if int(page) not in rules:
            continue
        for p in range(0, i):
            if int(order[p]) in rules[int(page)]:
                correct = False
    return correct

def sort_cmp(a, b):
    if int(a) not in rules:
        return 0
    if int(b) in rules[int(a)]:
        return -1
    return 1

rules = {}
sum_correct = 0
sum_ordered = 0
for l in fileinput.input():
    s = l.split("|")
    if len(s) == 2:
        rule = int(s[1])
        page = int(s[0])
        if page in rules:
            rules[page].append(rule)
        else:
            rules[page] = [rule]
    order = l.split(",")
    correct = True
    length = len(order)
    if len(order) < 2:
        continue
    if check_order(order, rules):
        sum_correct += int(order[int((length - 1) / 2)])
    else:
        order.sort(key=functools.cmp_to_key(sort_cmp))
        if check_order(order, rules):
            sum_ordered += int(order[int((length - 1) / 2)])

print(sum_correct)
print(sum_ordered)
