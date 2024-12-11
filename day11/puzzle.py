#!/usr/bin/env python

import fileinput, math

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            log = int(math.log10(stone))
            if log % 2 == 1:
                new_stones.append(int(stone / math.pow(10, int((log + 1)) / 2)))
                new_stones.append(int(stone % math.pow(10, int((log + 1)) / 2)))
            else:
                new_stones.append(stone * 2024)
    return new_stones

stones = []
for n in fileinput.input().readline().strip().split():
    stones.append(int(n))

for i in range(0, 25):
    stones = blink(stones)
print(len(stones))
