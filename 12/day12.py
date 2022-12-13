#!/bin/env python3

# Advent of Code 2022, Day 12

import datetime
import numpy as np


def node_index(row: int, col: int, num_cols: int):
    return row*num_cols + col


def min_distance(start_index: int, end_index: int, distances, 
        show_path=False):
    unvisited_nodes = set(range(len(distances)))
    d_star = [999 for i in range(len(distances))]
    prev_node = [999 for i in range(len(distances))]
    d_star[start_index] = 0

    while len(unvisited_nodes) > 0:
        min_unvisited_d_star = 1000
        for unvisited in unvisited_nodes:
            if d_star[unvisited] < min_unvisited_d_star:
                min_unvisited_d_star = d_star[unvisited]
                current_node = unvisited
        #print(f'current_node={current_node}')
        for unvisited in unvisited_nodes:
            if d_star[current_node] + distances[current_node][unvisited] \
                    < d_star[unvisited]:
                prev_node[unvisited] = current_node
                d_star[unvisited] = d_star[current_node] + \
                    distances[current_node][unvisited]
        unvisited_nodes.remove(current_node)
        if current_node == end_index:
            break

    if show_path==True:
        current = end_index
        print(f'{end_index}',end='')
        while current != start_index:
            print(f'<-{prev_node[current]}',end='')
            current = prev_node[current]
        print()
    return d_star[end_index]



if __name__ == '__main__':
    letters = "abcdefghijklmnopqrstuvwxyz"

    lines = open(0).read().rstrip('\n').split('\n')
    num_rows = len(lines)
    num_cols = len(lines[0])

    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter == 'S':
                start_index = node_index(row, col, num_cols)
                lines[row] = lines[row].replace('S','a')
                #print(f'after lines={lines[row]}')
            elif letter == 'E':
                end_index = node_index(row, col, num_cols)
                lines[row] = lines[row].replace('E','z')

    distances = [[999 for i in range(num_rows*num_cols)] for j in range(num_rows*num_cols)]
    for i in range(num_rows*num_cols):
        distances[i][i] = 0

    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            height = letters.index(letter)

            node = node_index(row, col, num_cols)
            if row > 0:
                up_height = letters.index(lines[row-1][col])
                up_node = node_index(row-1, col, num_cols)
                distances[node][up_node] = \
                        1 if up_height <= height + 1 else 999
            if row < num_rows-1:
                down_height = letters.index(lines[row+1][col])
                down_node = node_index(row+1, col, num_cols)
                distances[node][down_node] = \
                        1 if down_height <= height + 1 else 999
            if col > 0:
                left_height = letters.index(lines[row][col-1])
                left_node = node_index(row, col-1, num_cols)
                distances[node][left_node] = \
                        1 if left_height <= height + 1 else 999
            if col < num_cols-1:
                right_height = letters.index(lines[row][col+1])
                right_node = node_index(row, col+1, num_cols)
                distances[node][right_node] = \
                        1 if right_height <= height + 1 else 999

    unvisited_nodes = set(range(num_cols*num_rows))
    d_star = [999 for i in range(num_rows*num_cols)]
    prev_node = [999 for i in range(num_rows*num_cols)]
    d_star[start_index] = 0

    while len(unvisited_nodes) > 0:
        min_unvisited_d_star = 1000
        for unvisited in unvisited_nodes:
            if d_star[unvisited] < min_unvisited_d_star:
                min_unvisited_d_star = d_star[unvisited]
                current_node = unvisited
        #print(f'current_node={current_node}')
        for unvisited in unvisited_nodes:
            if d_star[current_node] + distances[current_node][unvisited] \
                    < d_star[unvisited]:
                prev_node[unvisited] = current_node
                d_star[unvisited] = d_star[current_node] + \
                    distances[current_node][unvisited]
        unvisited_nodes.remove(current_node)
        if current_node == end_index:
            break

    #print(f'd_star={d_star}')
    #print(f'prev_node = {prev_node}')

    #current = end_index
    #print(f'{end_index}',end='')
    #while current != start_index:
    #    print(f'<-{prev_node[current]}',end='')
    #    current = prev_node[current]
    #print()
    
    print('Part 1:')
    print(f"p1={min_distance(start_index, end_index, distances)}")

    # Floyd-Warshall algorithm -- takes more than 13 minutes to run
    t0 = datetime.datetime.now()
    distances = np.array(distances)
    for k in range(len(distances)):
        #print(f'Start k={k} at time {(datetime.datetime.now()-t0).seconds}')
        dk = distances[:,k].reshape((-1,1)) + distances[k,:].reshape((1,-1))
        distances[distances > dk] = dk[distances > dk]
        shortest_trail = 999
    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter=='a' and distances[row*num_cols+col][end_index] < shortest_trail:
                shortest_trail = distances[row*num_cols+col][end_index]

    print('Part 2:')
    print(f'p2={shortest_trail}')
