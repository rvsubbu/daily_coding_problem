#!/usr/bin/env python3

# This problem was asked by Bloomberg.

# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


import argparse
from collections import Counter

def run(word1, word2):
    '''
    Is a 1-to-1 mapping of word1 to word2 possible?
    Assumption; strings are of equal length
    '''
    if not word1 and not word2:
        return True

    if not word1 or not word2:
        return False
    if len(word1) != len(word2):
        return False

    counts1 = sorted(Counter(word1).values())
    counts2 = sorted(Counter(word2).values())

    if len(counts1) != len(counts1):
        return False

    for i in range(len(counts1)):
        if counts1[i] != counts2[i]:
            return False

    return True

def sanity_test():
    word1 = "abc"
    word2 = "bcd"
    assert(run(word1, word2))
    print("Sanity test 1 passed")

    word1 = "foo"
    word2 = "bar"
    assert(not run(word1, word2))
    print("Sanity test 2 passed")

def more_tests():
    tests = []
    for test in tests:
        res, word1, word2 = test
        assert(run(word1, word2) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 771: Determine whether 1-to-1 mapping of two words is possible')
    parser.add_argument('--word1', type=str)
    parser.add_argument('--word2', type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.word1 and args.word2:
        print("Word1 = ", word1, "Word2 = ", word2, "Result = ", run(args.word1, args.word2))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
