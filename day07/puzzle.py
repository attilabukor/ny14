#!/usr/bin/env python

import fileinput

def check(val, nums):
    res = [nums[0]]
    for n in nums[1:]:
        partial = []
        for r in res:
            partial.append(r * n)
            partial.append(r + n)
        res = partial

    if val in res:
        return True
    else:
        return False

part1 = 0
for l in fileinput.input():
    val, rest = l.strip().split(":")
    val = int(val)
    nums = []
    for n in rest.strip().split():
        n = int(n)
        nums.append(int(n))

    if check(val, nums):
        part1 += val

print(part1)
