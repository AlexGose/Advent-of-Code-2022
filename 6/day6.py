#!/bin/env python3

# Advent of Code 2022, Day 6


for line in open(0):
    for index, character in enumerate(line):
        if index >= 3:
            c1 = line[index-3]
            c2 = line[index-2]
            c3 = line[index-1]
            c4 = line[index]
            if not ( (c1==c2) or (c1==c3) or (c1==c4) or (c2==c3) or (c2==c4)
                    or (c3==c4)):
                print("start of packet at:", index+1)
                break
    for index, character in enumerate(line):
        if index >= 13:
            repeat_found = False
            for i in range(13):
                if line[index-i] in line[index-13:index-i-1] or \
                        line[index-i] in line[index-i+1:index+1]:
                            repeat_found = True
                            break
            if not repeat_found:
                print("start of message at:", index+1)
                break
