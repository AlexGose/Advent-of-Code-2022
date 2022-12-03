#!/bin/env python3

from pathlib import Path


def read_file(filename):
    lines = Path(filename).read_text().strip().split()
    return [priority(line) for line in lines]

def priority(line):
    number_of_items = len(line)
    compartment1 = line[:int(number_of_items/2)]
    compartment2 = line[int(number_of_items/2):]
    for item in compartment1:
        if item in compartment2:
            if item.isupper():
                return ord(item) - ord('A') + 27
            else:
                return ord(item) - ord('a') + 1

if __name__=='__main__':
    priorities = read_file('input')
    print(f'The sum of the priorities is {sum(priorities)}')
