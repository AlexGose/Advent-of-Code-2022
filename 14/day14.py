#!/bin/env python3

# Advent of Code 2022, Day 14

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates():
    x: int
    y: int

    def down(self):
        return Coordinates(self.x, self.y + 1)

    def left(self):
        return Coordinates(self.x - 1, self.y)

    def right(self):
        return Coordinates(self.x + 1, self.y)

    def sand_step(self, grid):
        if grid.air_at(self.down()):
            return self.down()
        elif grid.air_at(self.down().left()):
            return self.down().left()
        elif grid.air_at(self.down().right()):
            return self.down().right()
        else:
            return self


@dataclass
class Structure():
    coordinates: list

    def parse(text: str):
        return Structure([Coordinates(*map(int, c.split(',')))
            for c in text.split(' -> ')])

    def contains(self, coordinates):
        if len(self.coordinates)==1:
            #print(self)
            if coordinates == self.coordinates[0]:
                return True
            else:
                return False
        for index in range(len(self.coordinates)-1):
            x1 = self.coordinates[index].x
            y1 = self.coordinates[index].y
            x2 = self.coordinates[index+1].x
            y2 = self.coordinates[index+1].y
            if y1 == y2 == coordinates.y \
                    and min(x1,x2) <= coordinates.x <= max(x1,x2):
                return True
            elif x1 == x2 == coordinates.x \
                    and min(y1, y2) <= coordinates.y <= max(y1, y2):
                return True
        return False

    def max_y(self):
        return max(coord.y for coord in self.coordinates)

    def min_x(self):
        return min(coord.x for coord in self.coordinates)
    
    def max_x(self):
        return max(coord.x for coord in self.coordinates)


class Grid():
    num_rows: int
    num_cols: int
    min_x: int
    max_x: int
    max_y: int
    array: list

    def __init__(self, structures: list):
        self.min_x = min(struc.min_x() for struc in structures)
        self.max_x = max(struc.max_x() for struc in structures)
        self.max_y = max(struc.max_y() for struc in structures)
        self.array = [['.']*(self.max_y + 2) for i in range(self.max_x - self.min_x + 3)]
        #print(f'num rows = {len(self.array)}, num cols = {len(self.array[0])}')
        #print(f'max_y = {self.max_y}')
        #print(self)
        for struc in structures:
            self.add_stucture(struc)
            #print(self)
        #print(self)


    def get_grid_indices(self, coord):
        return coord.x - self.min_x + 1, coord.y 

    def add_stucture(self, struc, symbol='#'):
        if len(struc.coordinates) == 1:
            x1, y1 = self.get_grid_indices(struc.coordinates[0])
            self.array[x1][y1] = symbol
        else:
            for index in range(len(struc.coordinates)-1): 
                x1, y1 = self.get_grid_indices(struc.coordinates[index])
                x2, y2 = self.get_grid_indices(struc.coordinates[index + 1])
                if x1 == x2:
                    num_symbols = max(y1,y2) - min(y1,y2) + 1
                    self.array[x1][min(y1,y2):max(y1,y2)+1] = symbol * num_symbols
                elif y1 == y2:
                    for x in range(min(x1,x2), max(x1,x2) + 1):
                        self.array[x][y1] = symbol
                else:
                    raise ValueError(f'Invalid structure {struc}')
    
    def air_at(self, coordinates):
        x, y = self.get_grid_indices(coordinates)
        if self.array[x][y] == '.':
            return True
        else:
            return False

    def __repr__(self):
        output = ''
        for y in range(len(self.array[0])):
            for x in range(len(self.array)):
                output += self.array[x][y]
            output += f'{y}\n'
        return output


if __name__ == '__main__':
    lines = open(0).read().rstrip('\n').split('\n')
    structures = [Structure.parse(line) for line in lines]
    #print(structures)

    grid = Grid(structures)
    source = Coordinates(500, 0)
    grid.add_stucture(Structure([source]), symbol='+')
    units_of_sand = 0
    cave_filled = False
    while not cave_filled:
        sand = source
        while sand != sand.sand_step(grid):
            if sand.y >= grid.max_y:
                cave_filled = True
                break
            sand = sand.sand_step(grid)
        if sand == sand.sand_step(grid):
            units_of_sand += 1
            #print(f'Units of sand = {units_of_sand}.')
            grid.add_stucture(Structure([sand]), symbol='o')
            #print(structures)
            #print(sand)
    #print(grid)
    
    print(f'Part 1: {units_of_sand}')

    floor_y = grid.max_y + 2
    floor_x1 = 500 - floor_y - 2
    floor_x2 = 500 + floor_y + 2
    full_grid = Grid(structures + [Structure([Coordinates(floor_x1, floor_y),
        Coordinates(floor_x2, floor_y)])])
    source = Coordinates(500, 0)
    full_grid.add_stucture(Structure([source]), symbol='+')
    #print(full_grid)
    units_of_sand = 0
    flow_stopped = False
    while not flow_stopped:
        sand = source
        while sand != sand.sand_step(full_grid):
            sand = sand.sand_step(full_grid)
        if sand == source:
            flow_stopped = True
        units_of_sand += 1
        full_grid.add_stucture(Structure([sand]), symbol='o')
    #print(full_grid)
    print(f'Part 2: {units_of_sand}')
