#!/bin/env python3

# Advent of Code 2022, Day 8

import numpy as np


if __name__ == '__main__':
    p1=0
    p2=""

    tree_grid = []
    for line in open(0):
        line = line.rstrip('\n')
        tree_grid.append([-1]*len(line))
        for i in range(len(tree_grid[-1])):
            tree_grid[-1][i] = int(line[i])
    tree_grid = np.array(tree_grid)
    #print(tree_grid)

    num_rows, num_cols = tree_grid.shape

    max_top=-np.ones((num_rows, num_cols))
    max_bottom=-np.ones((num_rows, num_cols))
    max_left=-np.ones((num_rows, num_cols))
    max_right=-np.ones((num_rows, num_cols))

    max_top[1,:] = tree_grid[0, :]
    for row in range(2, num_rows):
        for col in range(num_cols):
            max_top[row,col] = max([max_top[row-1,col], tree_grid[row-1,col]])

    max_left[:,1] = tree_grid[:,0]
    for col in range(2, num_cols):
        for row in range(num_rows):
            max_left[row,col] = max([max_left[row,col-1], tree_grid[row,col-1]])

    max_bottom[-2,:] = tree_grid[-1, :]
    for row in range(num_rows-3, -1, -1):
        for col in range(num_cols):
            max_bottom[row, col] = max([max_bottom[row+1,col], tree_grid[row+1, col]])

    max_right[:,-2] = tree_grid[:, -1]
    for col in range(num_cols-3, -1, -1):
        for row in range(num_rows):
            max_right[row, col] = max([max_right[row, col+1], tree_grid[row, col+1]])

    for row in range(num_rows):
        for col in range(num_cols):
            if ( tree_grid[row,col] > max_top[row,col] ) \
                    | (tree_grid[row, col] > max_left[row, col]) \
                    | (tree_grid[row, col] > max_bottom[row, col]) \
                    | (tree_grid[row, col] > max_right[row, col]):
                p1 += 1

    print('Part1:')
    print(f'p1={p1}')

    print('Part2:')
    print(f'p2={p2}')
