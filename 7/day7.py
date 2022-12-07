#!/bin/env python3

# Advent of Code 2022, Day 7

from dataclasses import dataclass
from typing import Any 


@dataclass
class Directory():
    name: str
    parent: Any
    contents: dict
    size: int

    def get_parent(self):
        if self.name == '/':
            raise Exception("Root node has no parent")
        return self.parent

    def get_child(self, name):
        return self.contents[name]

    def add_file(self, name, size):
        self.contents[name] = File(name, size)
        self.size += size
        next_parent = self
        while next_parent.name != '/':
            next_parent = next_parent.get_parent()
            next_parent.size += size

    def add_dir(self, directory):
        self.contents[directory.name] = directory

    def __repr__(self):
        output = f"Directory(name={self.name},"
        output += f"parent={self.parent.name},size={self.size}\n"
        contents_string = ""
        for value in self.contents.values():
            for line in str(value).split('\n'):
                contents_string += " " + line + "\n"
        return output + contents_string.rstrip("\n")

    def get_total_size(self, max_size):
        output = 0
        if self.size < max_size:
            output += self.size
        for obj in self.contents.values():
            if isinstance(obj, Directory):
                output += obj.get_total_size(max_size)
        return output



@dataclass(frozen=True)
class File():
    name: str
    size: int


if __name__ == '__main__':
    root = Directory('/', None, {}, 0)
    root.parent = root
    current_dir = root
    for line in open(0):
        #print(line)
        line = line.rstrip('\n')
        if line.startswith('$ cd /'):
            current_dir = root
        elif line.startswith('$ cd'):
            if line[5:] == '..':
                current_dir = current_dir.get_parent()
            else:
                current_dir = current_dir.get_child(line[5:])
        elif not line.startswith('$'):
            info, name = line.split()
            if info == 'dir':
                current_dir.add_dir(Directory(name, current_dir, {}, 0))
            else:
                current_dir.add_file(name, int(info))

    total_sizes_under_100k = 0
    
    print('Part 1:')
    print(f'Sum of sizes below 100k: {root.get_total_size(100000)}')
