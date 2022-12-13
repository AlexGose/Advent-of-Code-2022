#!/bin/env python3

# Advent of Code 2022, day 13


class Packet():
    packet: list

    def __init__(self, packet):
        self.packet = packet

    def __eq__(self, other):
        if not isinstance(other, Packet):
            return False
        else:
            return self.packet == other.packet

    def __lt__(self, other):
        return self != other and in_order(self.packet, other.packet)


def in_order(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        if packet1 <= packet2:
            return True
        else:
            return False
    elif isinstance(packet1, int) and isinstance(packet2, list):
        return in_order([packet1],packet2)
    elif isinstance(packet1, list) and isinstance(packet2, int):
        return in_order(packet1, [packet2])
    elif len(packet1) == 0:
        return True
    elif len(packet2) == 0:
        return False
    else:
        for element1, element2 in zip(packet1, packet2):
            if element1 == element2:
                return in_order(packet1[1:], packet2[1:])
            else:
                return in_order(element1, element2)


if __name__ == '__main__':
    pairs_text = open(0).read().rstrip('\n').split('\n\n')
    pairs = [[] for i in range(len(pairs_text))]
    for index, pair in enumerate(pairs_text):
        first_text, second_text = pair.split('\n')
        pairs[index] = [eval(first_text), eval(second_text)]
        #print(pairs[index])

    p1 = 0
    for i, pair in enumerate(pairs):
        if in_order(pair[0],pair[1]):
            p1 += i+1
    print('Part 1:')
    print(f'p1={p1}')
    
    packets = [Packet([[2]]), Packet([[6]])]
    for pair in pairs:
        packets += [Packet(pair[0])]
        packets += [Packet(pair[1])]
    sorted_packets = sorted(packets)

    divider1 = sorted_packets.index(Packet([[2]]))+1
    divider2 = sorted_packets.index(Packet([[6]]))+1
    
    print('Part 2:')
    print(f'p2={divider1*divider2}')
