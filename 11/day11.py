#!/bin/env python3

# Advent of Code 2022, Day 11

from dataclasses import dataclass, field
from typing import Any
from collections import deque
import datetime


@dataclass
class Monkey():
    index: int
    operation: Any
    divisor: int
    monkey_for_true: int
    monkey_for_false: int
    number_inspected = 0
    items: Any = field(default_factory=deque)

    def copy(self):
        output = Monkey(self.index, self.operation, self.divisor,
                self.monkey_for_true, self.monkey_for_false,
                self.number_inspected)
        output.items = deque(item for item in self.items)
        return output

    def parse_text(text: str):
        lines = text.split('\n')
        index = int(lines[0].split()[1][:-1])
        items = eval('['+ lines[1][18:] + ']')
        items.reverse()
        #print(f'items: {items}')
        operation = eval('lambda ' + lines[2][13:].replace('new','old')
                .replace('=',':'))
        divisor = int(lines[3][21:])
        monkey_for_true = int(lines[4][29:])
        monkey_for_false = int(lines[5][30:])
        return Monkey(index, operation, divisor, monkey_for_true,
                monkey_for_false, deque(items))

    def receive_item(self, worry_level):
        self.items.appendleft(worry_level)


if __name__ == '__main__':
    monkeys_text = open(0).read().split('\n\n')
    monkeys = [Monkey.parse_text(text) for text in monkeys_text]
    monkeys2 = [monkey.copy() for monkey in monkeys]

    for round in range(20):
        for monkey in monkeys:
            #print(monkey)
            while len(monkey.items) > 0:
                worry_level = monkey.items.pop()
                monkey.number_inspected += 1
                worry_level = monkey.operation(worry_level)
                worry_level = worry_level // 3
                if worry_level % monkey.divisor == 0:
                    monkeys[monkey.monkey_for_true].receive_item(worry_level)
                else:
                    monkeys[monkey.monkey_for_false].receive_item(worry_level)

    largest = -1
    second_largest = -1
    for monkey in monkeys:
        number_inspected = monkey.number_inspected
        if number_inspected > largest:
            second_largest = largest
            largest = number_inspected
        elif number_inspected > second_largest:
            second_largest = number_inspected

    print('Part 1:')
    print(f'p1={largest*second_largest}')

    start_time = datetime.datetime.now()
    divisor_product = 1
    for monkey in monkeys2:
        divisor_product *= monkey.divisor
    for round in range(10000):
        number_of_passes = 0
        for monkey in monkeys2:
            #print(monkey)
            while len(monkey.items) > 0:
                worry_level = monkey.items.pop()
                number_of_passes += 1
                monkey.number_inspected += 1
                worry_level = monkey.operation(worry_level)
                worry_level = worry_level % divisor_product
                if worry_level % monkey.divisor == 0:
                    monkeys2[monkey.monkey_for_true].receive_item(worry_level)
                else:
                    monkeys2[monkey.monkey_for_false].receive_item(worry_level)
        #if ((round+1) % 10) == 0:
        #    current_time = datetime.datetime.now()
        #    print(f'Elapsed time after {round+1} rounds: ', end='')
        #    print(f'{(current_time - start_time).seconds}')
        #    print(f'Number of passes in last round: {number_of_passes}')
        #    #print(f'First monkey: {monkeys2[0]}')
        #    #print(f'first monkey item 0: {monkeys2[0].items[0]}')
        if (round == 0) or (round == 19) or (((round+1) % 1000) == 0):
            print(f'== After round {round + 1} ==')
            for monkey in monkeys2:
                print(f'monkey {monkey.index} inspected items {monkey.number_inspected} times.')

    largest = -1
    second_largest = -1
    for monkey in monkeys2:
        number_inspected = monkey.number_inspected
        if number_inspected > largest:
            second_largest = largest
            largest = number_inspected
        elif number_inspected > second_largest:
            second_largest = number_inspected

    print('Part 2:')
    print(f'p2={largest*second_largest}')

