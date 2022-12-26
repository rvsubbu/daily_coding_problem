#!/usr/bin/env python3

#This problem was asked by Amazon.

#Given a string, determine whether any permutation of it is a palindrome.

#For example, "carrace" should return true, since it can be rearranged to form racecar, which is a palindrome. "daily" should return false, since there's no rearrangement that can form a palindrome.

import argparse
from collections import Counter

def run(word):
    '''
    Check whether any permutation of the word can be a palindrome
    keyword args:
    word -- word to check
    '''
 
    counter = Counter(word)
    odd_counts = 0
    for letter, count in counter.items():
        if count % 2 == 1:
            if odd_counts == 1:
                return False
            odd_counts += 1
    return True

def sanity_test():
    assert(run("carrace"))
    print("Sanity test 1 args: word=carrace can be a palindrome")
    assert(not run("daily"))
    print("Sanity test 2 args: word=daily cannot be a palindrome")

    print("Sanity tests passed")

def more_tests():
    tests = [
    ]
    for test in tests:
        res, word = test
        #print("word=", word, "expected=", res, "got=", run(word))
        assert(run(k) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 868; check word for palindrome-ness')
    parser.add_argument('-w', help='Word to check for palindrome-ness', type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.w:
        if run(args.w):
            print(args.w + " can be permuted to a palindrome")
        else:
            print(args.w + " cannot be permuted to a palindrome")
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
