#!/usr/bin/env python3

# This problem was asked by Jane Street.

# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.

import argparse
from collections import deque

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def run(rpn_elements):
    '''
    Check whether any permutation of the word can be a palindrome
    keyword args:
    rpn_elements -- Queue of nums and ops
    '''
 
    nums = deque()

    for element in rpn_elements:
        if isinstance(element, float):
            nums.append(element)
        elif isinstance(element, int):
            nums.append(element)
        else:
            num1 = nums.pop()
            num2 = nums.pop()
            if element == "+":
                nums.append(num1+num2)
            elif element == "-":
                nums.append(num1-num2)
            elif element == "*":
                nums.append(num1*num2)
            elif element == "/":
                nums.append(float(num1)/float(num2))
    return nums.pop()

def sanity_test():
    test1 = [5, 3, "+"]
    assert(run(test1) == 8)
    print("Sanity test 1 passed: 5+3 = 8")
    test2 = [15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"]
    assert(run(test2) == 5)
    print("Sanity test 2 passed: (15/(7-(1+1)))*3)-(2+(1+1)) = 5")

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
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 873: Calculator with Reverse Polish Notation')
    parser.add_argument('-e', '--elements', nargs="+", type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.elements:
        rpn_elements = [float(a) if is_float(a) else a for a in args.elements]
        res = run(rpn_elements)
        print("Result of <" + " ".join(args.elements) + "> is " + str(res))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
