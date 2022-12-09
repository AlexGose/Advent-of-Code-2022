#!/bin/env python3

# Advent of Code 2022, Day 9

from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates():
    x: int = 0
    y: int = 0


@dataclass
class Position():
    x: int = 0
    y: int = 0

    def move_to_head(self, head: Coordinates):
        dx = head.x - self.x
        dy = head.y - self.y
        if  ( -1 <= dx <= 1 ) and ( -1 <= dy <= 1 ):
            return
        elif ( -2 <= dx <= 2 ) and ( dy == 0):
            self.x += dx // 2
        elif ( -2 <= dy <= 2 ) and ( dx == 0):
            self.y += dy // 2
        elif ( -2 <= dy <= 2 ) and ( -2 <= dx <= 2 ):
            self.y += dy // abs(dy)
            self.x += dx // abs(dx)
        else:
            raise ValueError(f"Invalid coordinates {head}")

    def move(self, direction: str):
        if direction == 'L':
            self.x -= 1
        elif direction == 'U':
            self.y += 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'D':
            self.y -= 1

    def get_coordinates(self):
        return Coordinates(self.x, self.y)


if __name__ == '__main__':

    lines = open(0).read().strip('\n').split('\n')
    moves = ""
    for line in lines:
        moves += line[0]*int(line[1:])
    #print(moves)
    
    head = Position()
    tail = Position()
    visited_coordinates = set()
    visited_coordinates.add(Coordinates())
    for move in moves:
        head.move(move)
        tail.move_to_head(head)
        #print(f"tail visits: {tail.get_coordinates()}")
        visited_coordinates.add(tail.get_coordinates())

    #print(len(visited_coordinates))

    print('Part 1:')
    print(f'p1={len(visited_coordinates)}')

    p2 = 0
    print()
    print('Part 2:')
    print(f'p2={p2}')
