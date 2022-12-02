#!/bin/env python3

# Advent of Code 2022 Problem 2 part 1 (Rock Paper Scissors Tournament)

from pathlib import Path


class Shape():
    def __init__(self, letter):
        self.letter = letter

    def is_rock(self):
        return self.letter == 'R'

    def is_paper(self):
        return self.letter == 'P'

    def is_scissors(self):
        return self.letter == 'S'

    def decode_your(letter, opponent_shape=None):
        if opponent_shape == None:
            if letter == 'X':
                return Shape('R')
            elif letter == 'Y':
                return Shape('P')
            elif letter == 'Z':
                return Shape('S')
        else:
            if letter == 'X':
                return opponent_shape.get_worse_shape()
            elif letter == 'Y':
                return opponent_shape
            elif letter == 'Z':
                return opponent_shape.get_better_shape()

    def get_better_shape(self):
        if self.is_rock():
            return Shape('P')
        elif self.is_paper():
            return Shape('S')
        elif self.is_scissors():
            return Shape('R')

    def get_worse_shape(self):
        if self.is_rock():
            return Shape('S')
        if self.is_paper():
            return Shape('R')
        if self.is_scissors():
            return Shape('P')

    def decode_opponent(letter):
        if letter == 'A':
            return Shape('R')
        elif letter == 'B':
            return Shape('P')
        elif letter == 'C':
            return Shape('S')

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.letter == other.letter

    def __lt__(self, other):
        if isinstance(other, Shape):
            return ( (self.letter == 'R') & (other.letter == 'P') ) \
                    | ( ( self.letter == 'P') & (other.letter == 'S') ) \
                    | ( ( self.letter == 'S') & (other.letter == 'R') )
        return False


class Round():
    def read_file_part1(filename):
        p = Path(filename)
        lines = p.read_text().strip().split('\n')
        return [Round.decode_string_part1(line) for line in lines]

    def read_file_part2(filename):
        p = Path(filename)
        lines = p.read_text().strip().split('\n')
        return [Round.decode_string_part2(line) for line in lines]

    def decode_string_part1(line):
        opponent_shape = Shape.decode_opponent(line[0])
        your_shape = Shape.decode_your(line[-1])
        return Round(opponent_shape, your_shape)

    def decode_string_part2(line):
        opponent_shape = Shape.decode_opponent(line[0])
        your_shape = Shape.decode_your(line[-1], opponent_shape)
        return Round(opponent_shape, your_shape)

    def __init__(self, opponent_shape, your_shape):
        self.opponent_shape = opponent_shape
        self.your_shape = your_shape

    def your_shape_points(self):
        if self.your_shape.is_rock():
            return 1
        elif self.your_shape.is_paper():
            return 2
        elif self.your_shape.is_scissors():
            return 3

    def your_win_loss_points(self):
        if self.your_shape < self.opponent_shape:
            return 0
        elif self.your_shape == self.opponent_shape:
            return 3
        elif self.your_shape > self.opponent_shape:
            return 6

    def your_total_points(self):
        return self.your_shape_points() + self.your_win_loss_points()


def print_total_score(rounds):
    total_score = 0
    for r in rounds:
        total_score += r.your_total_points()
    print(f"total score is {total_score}")


if __name__=='__main__':
    print('Part 1:')
    rounds = Round.read_file_part1('input')
    print_total_score(rounds)
    
    print('Part 2:')
    rounds = Round.read_file_part2('input')
    print_total_score(rounds)
