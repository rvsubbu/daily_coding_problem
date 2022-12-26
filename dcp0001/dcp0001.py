#!/usr/bin/env python3

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


import argparse
from collections import Counter

def run(k, nums):
    '''
    Two-sum problem
    keyword args:
    k -- Target sum
    nums -- sequence of nums
    '''
    if not nums:
        return 0

    map = {}
    for num in nums:
        if num in map:
            return True
        map[k-num] = True
    return False

def sanity_test():
    k = 17
    nums = [10, 15, 3, 7]
    assert(run(k, nums))
    print("Sanity test args: k=", k, "nums=", nums)
    print("Sanity test passed")

def more_tests():
    tests = []
    for test in tests:
        res, k, nums = test
        #print("k=", k, "nums=", nums, "expected=", res, "got=", run(k, nums))
        assert(run(k, nums) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 1: Two Sum')
    parser.add_argument('-k', help='Target Sum', type=int)
    parser.add_argument('-n', '--nums', nargs="+", type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.k:
        print("Result = ", run(args.k, args.nums))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
