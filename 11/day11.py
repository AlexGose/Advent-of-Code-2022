#!/bin/env python3

# Advent of Code 2022, Day 11

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Monkey():
    index: int
    operation: Any
    divisor: int
    monkey_for_true: int
    monkey_for_false: int
    number_inspected = 0
    items: list = field(default_factory=list)

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
                monkey_for_false, items)

    def receive_item(self, worry_level):
        self.items.insert(0, worry_level)


if __name__ == '__main__':
    monkeys_text = open(0).read().split('\n\n')
    monkeys = []
    for text in monkeys_text:
        monkeys.append(Monkey.parse_text(text))

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
