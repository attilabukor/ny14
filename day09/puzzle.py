#!/usr/bin/env python

import fileinput

disk_map = []
file_id = 0
free = False
for c in fileinput.input().readline().strip():
    for i in range(0, int(c)):
        if free:
            disk_map.append(None)
        else:
            disk_map.append(file_id)
    free = not free
    if free:
        file_id += 1

full_idx = 0

for i in range(len(disk_map) - 1, -1, -1):
    if disk_map[i] != None:
        for j in range(full_idx, i):
            if disk_map[j] == None:
                full_idx = j - 1
                disk_map[j] = disk_map[i]
                disk_map[i] = None
                break

checksum = 0
for idx, file_id in enumerate(disk_map):
    if file_id == None:
        break
    checksum += idx * file_id


print(checksum)
