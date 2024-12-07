#!/usr/bin/env python

import fileinput

def check(val, nums, concat):
    res = [nums[0]]
    for n in nums[1:]:
        partial = []
        for r in res:
            partial.append(r * n)
            partial.append(r + n)
            if concat:
                partial.append(int(str(r) + str(n)))
        res = partial

    if val in res:
        return True
    else:
        return False

part1 = 0
part2 = 0
for l in fileinput.input():
    val, rest = l.strip().split(":")
    val = int(val)
    nums = []
    for n in rest.strip().split():
        n = int(n)
        nums.append(int(n))

    if check(val, nums, False):
        part1 += val
    if check(val, nums, True):
        part2 += val

print(part1)
print(part2)
