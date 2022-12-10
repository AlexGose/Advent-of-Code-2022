#!/bin/env python3

# Advent of code 2022, day 10


def print_screen(crt):
    for row in crt:
        for col in row:
            print(col, end='')
        print()


if __name__ == '__main__':
    lines = open(0).read().rstrip('\n').split('\n')

    X = 1
    addx = 0
    signal_strength = 0
    cycle = 0
    p1=0
    cycles_left = 0
    CRT = [['X' for col in range(40)] for row in range(6)]
    row = 0
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
                #print(f'cycle={cycle}, signal_strength={signal_strength}')
            row = (cycle-1) // 40 % 6
            col = (cycle-1) % 40
            #print('row=',row,'col=',col,'X=',X)
            if X-1 <= col <= X+1:
                CRT[row][col] = '#'
                #print(f'CRT[row][col]={CRT[row][col]}')
            else:
                CRT[row][col] = '.'
            #print_screen(CRT)
            cycles_left -= 1
            if cycles_left == 0:
                X += addx

    print('Part 1:')
    print(f'p1={p1}')

    print('Part 2:')
    print_screen(CRT)
