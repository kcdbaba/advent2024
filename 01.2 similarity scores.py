#!/usr/bin/env python

def iter_input():
    with open('inputs/day1') as f:
        for line in f:
            nums = line.split()
            yield tuple(int(n) for n in nums)

def get_location_counts():
    left_ids, right_ids = tuple(zip(*iter_input()))
    right_counts = {}
    for loc_id in right_ids:
        right_counts[loc_id] = right_counts.get(loc_id, 0) + 1
    return left_ids, right_counts

def similarity_scores():
    left_ids, right_counts = get_location_counts()
    for left_id in left_ids:
        yield left_id * right_counts.get(left_id, 0)

if __name__ == '__main__':
    print('Day 1, Part 2:', sum(similarity_scores()))