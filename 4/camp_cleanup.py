#!/bin/bash

# Advent of Code 2022, Day 4: Camp Cleanup

from pathlib import Path
from dataclasses import dataclass


def parse_data(filename: str):
    lines = Path(filename).read_text().strip().split()
    output = [[(),()]] * len(lines)
    for line_index, line in enumerate(lines):
        first_range_text, second_range_text = line.split(',')
        output[line_index] = [Range.parse(first_range_text), \
                Range.parse(second_range_text)]
    return output


@dataclass(frozen=True)
class Range():
    lower_limit: int
    upper_limit: int

    def parse(text: str):
        lower_text, upper_text = text.split('-')
        return Range(int(lower_text), int(upper_text))

    def contains(self, other) -> bool:
        if ( other.lower_limit >= self.lower_limit ) & \
                ( other.upper_limit <= self.upper_limit ):
            return True
        return False


if __name__ == '__main__':
    lines = parse_data('input')
    contained_pair_count = 0
    for ranges in lines:
        if ranges[0].contains(ranges[1]) | ranges[1].contains(ranges[0]):
            contained_pair_count += 1
    print('Part 1')
    print(f'Total pairs with containment: {contained_pair_count}')
