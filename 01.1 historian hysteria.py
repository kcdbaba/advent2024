#!/usr/bin/env python

def iter_input():
    with open('inputs/day1') as f:
        for line in f:
            nums = line.split()
            yield tuple(int(n) for n in nums)

def pair_distance(left, right):
    return abs(right - left)

def iter_sorted_locations():
    left_ids, right_ids = tuple(zip(*iter_input()))
    for left, right in zip(sorted(left_ids), sorted(right_ids)):
        yield pair_distance(left, right)


if __name__ == '__main__':
    print('Day 1, Part 1:', sum(iter_sorted_locations()))
