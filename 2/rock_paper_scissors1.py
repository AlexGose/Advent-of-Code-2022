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


class Round():
    def __init__(self, shapes):
        self.shapes = ' '.join(shapes)

    def your_shape_points(self):
        if self.your_shape() == 'R':
            return 1
        elif self.your_shape() == 'P':
            return 2
        elif self.your_shape() == 'S':
            return 3

    def your_shape(self):
        return self.shapes[-1]
    
    def your_win_loss_points(self):
        if (self.shapes == 'S R') | (self.shapes == 'R P') \
                | (self.shapes ==  'P S'):
            return 6
        elif (self.shapes == 'R R') | (self.shapes == 'P P') \
                | (self.shapes == 'S S'):
            return 3
        else:
            return 0

    def your_total_points(self):
        return self.your_shape_points() + self.your_win_loss_points()


if __name__=='__main__':
    strategy_guide = parse_data('input')

    total_score = 0
    for decoded_string in strategy_guide:
        r = Round(decoded_string)
        # print(f'r.your_win_loss_points()={r.your_win_loss_points()}')
        total_score += r.your_total_points()

    print(f"total score is {total_score}")
