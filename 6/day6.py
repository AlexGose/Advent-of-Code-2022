#!/bin/env python3

# Advent of Code 2022, Day 6
import timeit

def message_start_index(line):
    for index, character in enumerate(line):
        if index >= 13:
            repeat_found = False
            for i in range(13):
                if line[index-i] in line[index-13:index-i-1] or \
                        line[index-i] in line[index-i+1:index+1]:
                            repeat_found = True
                            break
            if not repeat_found:
                return index + 1


def message_start_index_faster(line):
    index = 1
    prev_repeat = -1
    while index < len(line):
        repeat_index = line.find(line[index], prev_repeat+1, index)
        if repeat_index == -1 and index - prev_repeat >= 14:
            return index + 1
        
        if repeat_index > -1:
            prev_repeat = repeat_index
        index += 1


if __name__ == '__main__':
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

        p2 = message_start_index(line)
        p22 = message_start_index_faster(line)
        print('  runtime for message_start_index:')
        print(timeit.repeat('message_start_index(line)', number=100, globals=globals()))
        print('  runtime for message_start_index_faster:')
        print(timeit.repeat('message_start_index_faster(line)', number=100, globals=globals()))
        print("start of message at:", p2, "and", p22)
