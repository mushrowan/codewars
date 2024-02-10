#!/usr/bin/python3
# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    unique_nums = set(seq)
    for i in unique_nums:
        if seq.count(i) % 2 != 0:
            return i
