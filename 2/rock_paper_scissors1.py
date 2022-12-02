#!/bin/env python3

# Advent of Code 2022 Problem 2 part 1 (Rock Paper Scissors Tournament)

from pathlib import Path


def parse_data(filename):
    p = Path(filename)
    strategy = p.read_text().strip().split('\n')
    strategy = [decode(s.split()) for s in strategy]
    return strategy


def decode(encoded_round):
    decoded_round = ['', '']
    if encoded_round[0] == 'A':
        decoded_round[0] = 'R'
    elif encoded_round[0] == 'B':
        decoded_round[0] = 'P'
    elif encoded_round[0] == 'C':
        decoded_round[0]  = 'S'

    if encoded_round[1] == 'X':
        decoded_round[1] = 'R'
    elif encoded_round[1] == 'Y':
        decoded_round[1] = 'P'
    elif encoded_round[1] == 'Z':
        decoded_round[1] = 'S'

    return decoded_round


def get_points(decoded_round):
    points = 0
    if decoded_round[1] == 'R':
        points += 1
        if decoded_round[0]=='R':
            points += 3
        elif decoded_round[0]=='S':
            points += 6
    elif decoded_round[1] == 'P':
        points += 2
        if decoded_round[0] == 'P':
            points += 3
        elif decoded_round[0] == 'R':
            points += 6
    elif decoded_round[1] == 'S':
        points += 3
        if decoded_round[0] == 'S':
            points += 3
        elif decoded_round[0] == 'P':
            points += 6
    return points


if __name__=='__main__':
    strategy_guide = parse_data('input')

    total_score = 0
    for decoded_round in strategy_guide:
        total_score += get_points(decoded_round)

    print(f"total score is {total_score}")
