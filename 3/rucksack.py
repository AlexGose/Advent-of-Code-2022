#!/bin/env python3

from pathlib import Path


def read_file(filename):
    return Path(filename).read_text().strip().split()


def sum_bag_priorities(filename):
    priority_sum = 0
    lines = read_file(filename)
    for line in lines:
        compartment1, compartment2 = get_compartments(line)
        item = common_item(compartment1, compartment2)
        priority_sum += priority(item)
    return priority_sum


def sum_group_priorities(filename):
    priority_sum = 0
    lines = read_file(filename)
    for row_index in range(0, len(lines), 3):
        badge = get_badge(lines[row_index], lines[row_index+1],
                lines[row_index+2])
        priority_sum += priority(badge)
    return priority_sum


def get_compartments(line):
    number_of_items = len(line)
    compartment1 = line[:int(number_of_items/2)]
    compartment2 = line[int(number_of_items/2):]
    return compartment1, compartment2


def common_item(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item


def get_badge(line1, line2, line3):
    for item in line1:
        if ( item in line2 ) & ( item in line3 ):
            return item
    raise Exception(f"item {item} not found")


def priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


if __name__=='__main__':
    filename = 'input'

    print('Part 1:')
    print(f'The sum of the priorities is {sum_bag_priorities(filename)}')

    print('Part 2:')
    print(f'The sum of the priorities is {sum_group_priorities(filename)}')
