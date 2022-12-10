#!/bin/env python3

# Advent of code 2022, day 10

if __name__ == '__main__':
    lines = open(0).read().rstrip('\n').split('\n')

    X = 1
    addx = 0
    signal_strength = 0
    cycle = 0
    p1=0
    cycles_left = 0
    for line in lines:
        if line[0:4] == 'noop':
            cycles_left = 1
            addx = 0
        else:
            cycles_left = 2
            addx = int(line[5:])

        while cycles_left > 0:
            cycle += 1
            signal_strength = cycle * X
            if (cycle - 20) % 40 == 0:
                p1 += signal_strength
                print(f'cycle={cycle}, signal_strength={signal_strength}')
            cycles_left -= 1
        X += addx

    print('Part 1:')
    print(f'p1={p1}')
    
    p2=0
    print()
    print('Part 2:')
    print(f'p2={p2}')
