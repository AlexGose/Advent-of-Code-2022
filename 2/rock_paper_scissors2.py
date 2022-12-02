#!/bin/env python3

# Advent of Code 2022 Problem 2 part 2 (Rock Paper Scissors Tournament)

from pathlib import Path


def parse_data(filename):
    p = Path(filename)
    strategy = p.read_text().strip().split('\n')
    strategy = [decode(s.split()) for s in strategy]
    return strategy


def lose(opponent_shape):
    if opponent_shape == 'R':
        return 'S'
    elif opponent_shape == 'P':
        return 'R'
    elif opponent_shape == 'S':
        return 'P'
    else:
        raise ValueError('Invalid opponent shape')


def draw(opponent_shape):
    return opponent_shape


def win(opponent_shape):
    if opponent_shape == 'R':
        return 'P'
    elif opponent_shape == 'P':
        return 'S'
    elif opponent_shape == 'S':
        return 'R'
    else:
        raise ValueError('Invalid opponent shape')


def decode(encoded_round):
    decoded_round = ['', '']
    if encoded_round[0] == 'A':
        decoded_round[0] = 'R'
    elif encoded_round[0] == 'B':
        decoded_round[0] = 'P'
    elif encoded_round[0] == 'C':
        decoded_round[0]  = 'S'

    if encoded_round[1] == 'X':
        decoded_round[1] = lose(decoded_round[0])
    elif encoded_round[1] == 'Y':
        decoded_round[1] = draw(decoded_round[0])
    elif encoded_round[1] == 'Z':
        decoded_round[1] = win(decoded_round[0])

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
