#!/bin/env python3

# Advent of Code 2022, Day 15

from dataclasses import dataclass, field
from typing import Any



@dataclass(frozen=True)
class Position():
    x: int
    y: int

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class Sensor():
    location: Any
    closest_beacon: Any
    distance_to_closest_beacon: int = field(default=-1, repr=False)

    def parse(text):
        tokens = text.split()
        loc_x = int(tokens[2][2:-1])
        loc_y = int(tokens[3][2:-1])
        b_x = int(tokens[8][2:-1])
        b_y = int(tokens[9][2:])
        return Sensor(Position(loc_x, loc_y), Position(b_x, b_y))

    def max_closest_beacon_distance(sensors):
        return max([sensor.location.distance_to(sensor.closest_beacon) for
                sensor in sensors])

    def closest_beacon_distance(self):
        if self.distance_to_closest_beacon == -1:
            self.distance_to_closest_beacon = \
                    self.location.distance_to(self.closest_beacon)
        return self.distance_to_closest_beacon

    def interval(self, y):
        interval_width = self.closest_beacon_distance() \
                    - abs(self.location.y - y)
        if interval_width >= 0:
            return (self.location.x - interval_width, 
                    self.location.x + interval_width)
        else:
            return None


def beacon_x_values(sensors):
    output = set()
    for sensor in sensors:
        if sensor.closest_beacon.y == y:
            output.add(sensor.closest_beacon.x)
    return list(output)


def no_beacon_intervals(sensors, y):
    intervals = []
    for sensor in sensors:
        if abs(sensor.location.y - y) <= sensor.closest_beacon_distance():
            half_width = sensor.closest_beacon_distance() \
                    - abs(sensor.location.y - y)
            x_interval_left = sensor.location.x - half_width
            x_interval_right = sensor.location.x + half_width
            intervals.append((x_interval_left,x_interval_right))
    #print(intervals)

    intervals_combined = True
    while intervals_combined:
        intervals_combined = False
        for i, interval in enumerate(intervals):
            for j, next_interval in enumerate(intervals[i+1:]):
                if ( next_interval[0] <= interval[0] and
                    interval[1] <= next_interval[1] ):
                    intervals.remove(interval)
                    intervals_combined = True
                    break
                elif ( interval[0] <= next_interval[0] and
                    next_interval[1] <= interval[1] ):
                    intervals.remove(next_interval)
                    intervals_combined = True
                elif ( next_interval[0] <= interval[0] <= next_interval[1] ):
                    intervals.append((next_interval[0], interval[1]))
                    intervals.remove(interval)
                    intervals.remove(next_interval)
                    intervals_combined = True
                    break
                elif ( next_interval[0] <= interval[1] <= next_interval[1] ):
                    intervals.append((interval[0], next_interval[1]))
                    intervals.remove(interval)
                    intervals.remove(next_interval)
                    intervals_combined = True
                    break
    return intervals


def covered_x(intervals, min_x, max_x):
    count = 0
    x = min_x
    uncovered_x = -1
    while x <= max_x:
        for i, interval in enumerate(intervals):
            if interval and interval[0] <= x <= interval[1]:
                count += min(interval[1], max_x) - x + 1
                x = min(interval[1], max_x)
                #print(f'count = {count}, x= {x}')
                break
            if i == len(intervals) - 1:
                print(f'uncovered point found at x={x}')
                uncovered_x = x
        x += 1
        #print(f'count = {count}, x= {x}')
    return count, uncovered_x


if __name__ == '__main__':
    lines = open(0).read().rstrip('\n').split('\n')
    if len(lines) == 14:
        y = 10
        y_max = 20
    else:
        y = 2000000
        y_max = 4000000

    sensors = [Sensor.parse(line) for line in lines]

    beacon_x = beacon_x_values(sensors)
    #print(beacon_x)

    intervals = no_beacon_intervals(sensors, y)

    num_without_beacon = 0
    for interval in intervals:
        num_without_beacon += interval[1] - interval[0] + 1
        for x in beacon_x:
            if interval[0] <= x <= interval[1]:
                num_without_beacon -= 1
                beacon_x.remove(x)

    print(f'Part 1: {num_without_beacon}')

    for y in range(y_max+1):
        intervals = [sensor.interval(y) for sensor in sensors]
        count, uncovered_x = covered_x(intervals, 0, y_max)
        if count < y_max+1:
            print(f'uncovered point found at y={y}')
            print(f'Part 2: tuning frequency = {uncovered_x*4000000 + y}')
            break
