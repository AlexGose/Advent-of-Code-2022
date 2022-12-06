#!/bin/env python3

# Advent of Code 2022, Day 5: Supply Stacks
# Goal: readability

from pathlib import Path
from dataclasses import dataclass


@dataclass
class Stack():
    crate_names: list 
    index: int

    def remove(self, number_to_remove):
        crates_removed = self.crate_names[-number_to_remove:]
        self.crate_names = self.crate_names[:-number_to_remove]
        return crates_removed

    def add(self, crate_labels: list):
        self.crate_names.extend(crate_labels)

    def parse_stacks(text: str):
        lines = text.rstrip('\n').split('\n')
        crate_labels_str = lines[:-1]
        stack_numbers_str = lines[-1].strip().split()
        stack_numbers = list(map(int, stack_numbers_str))

        stacks = [Stack([], number) for number in stack_numbers]

        for index, number in enumerate(stack_numbers):
            string_index = lines[-1].index(str(number))
            for row in range(len(crate_labels_str)-1, -1, -1):
                if crate_labels_str[row][string_index] != ' ':
                    stacks[index].add([crate_labels_str[row][string_index]])
        return stacks

    def copy(self):
        return Stack([name for name in self.crate_names], self.index)

    def top_crate(self):
        return self.crate_names[-1]


@dataclass(frozen=True)
class Move():
    number_of_crates: int
    from_index: int
    to_index: int

    def parse_move(text: str):
        number_of_crates, from_index, to_index = map(int, text.rstrip('\n')
                    .replace('move','')
                    .replace('from','')
                    .replace('to','')
                    .strip()
                    .split())
        return Move(number_of_crates, from_index, to_index)

    def parse_moves(lines: str):
        return [Move.parse_move(line) for line in lines.strip().split('\n')]

    def move_one_by_one(self, stacks):
        stack_indices = [stack.index for stack in stacks]
        from_stack = stacks[stack_indices.index(self.from_index)]
        to_stack = stacks[stack_indices.index(self.to_index)]
        for crate in range(self.number_of_crates):
            crate_label = from_stack.remove(1)
            to_stack.add(crate_label)
        return stacks

    def move_in_groups(self, stacks):
        stack_indices = [stack.index for stack in stacks]
        from_stack = stacks[stack_indices.index(self.from_index)]
        to_stack = stacks[stack_indices.index(self.to_index)]
        crate_labels = from_stack.remove(self.number_of_crates)
        to_stack.add(crate_labels)
        return stacks


if __name__ == '__main__':
    filename = 'input'

    raw_stacks_data, raw_moves_data = Path(filename).read_text().split('\n\n')
    
    stacks = Stack.parse_stacks(raw_stacks_data)
    stacks2 = [stack.copy() for stack in stacks]
    moves = Move.parse_moves(raw_moves_data)
    
    print('Part 1')
    for move in moves:
        stacks = move.move_one_by_one(stacks)
    for stack in stacks:
        print(stack.top_crate(), end='') 
    print()

    print('Part 2')
    for move in moves:
        stacks2 = move.move_in_groups(stacks2)
    for stack in stacks2:
        print(stack.top_crate(), end='')
    print()
