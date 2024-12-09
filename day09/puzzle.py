#!/usr/bin/env python

import fileinput

def draw(disk_map, pos=None):
    for c in disk_map:
        if c == None:
            print(".", end="")
        else:
            print(c, end="")
    print()
    if pos != None:
        for c in range(0, pos):
            print(" ", end="")
        print("^")

def pt1(disk_map):
    full_idx = 0
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != None:
            for j in range(full_idx, i):
                if disk_map[j] == None:
                    full_idx = j - 1
                    disk_map[j] = disk_map[i]
                    disk_map[i] = None
                    break
    return disk_map

def pt2(disk_map):
    empties = {}
    empty_start = None
    for i in range(0, len(disk_map)):
        if disk_map[i] == None and (i == 0 or disk_map[i - 1] != None):
            empty_start = i
        elif disk_map[i] != None and i > 0 and disk_map[i - 1] == None:
            empties[empty_start] = i - empty_start

    size = 0
    file_id = None
    for i in range(len(disk_map) - 1, -1, -1):
        if file_id == disk_map[i]:
            size += 1
        else:
            if file_id != None:
                for idx in sorted(empties.keys()):
                    if empties[idx] >= size and idx < i:
                        for j in range(0, size):
                            disk_map[idx + j] = disk_map[i + j + 1]
                            disk_map[i + j + 1] = None
                        empties[idx + size] = empties[idx] - size
                        empties[idx] = 0
                        break
            size = 1
            file_id = disk_map[i]

    return disk_map

def checksum(disk_map):
    checksum = 0
    for idx, file_id in enumerate(disk_map):
        if file_id != None:
            checksum += idx * file_id
    return checksum

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


#print(checksum(pt1(disk_map)))
print(checksum(pt2(disk_map)))
