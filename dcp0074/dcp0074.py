#!/usr/bin/env python3

# This problem was asked by Apple.

# Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

# Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

# For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

# | 1 | 2 | 3 | 4 | 5 | 6 |
# | 2 | 4 | 6 | 8 | 10 | 12 |
# | 3 | 6 | 9 | 12 | 15 | 18 |
# | 4 | 8 | 12 | 16 | 20 | 24 |
# | 5 | 10 | 15 | 20 | 25 | 30 |
# | 6 | 12 | 18 | 24 | 30 | 36 |

# And there are 4 12's in the table.


import argparse
import math

def run(x, n):
    '''
    keyword args:
    x -- Value to check for in multiplication tables
    n -- max multiplication table
    '''

    threshold = int(math.sqrt(x))
    if threshold > n:
        threshold = n
    divisors_of_x = [y for y in range(1,threshold+1) if x%y==0]
    ret = len(divisors_of_x)
    for i in divisors_of_x:
        if x/i <= n:
            if i*i != x:
                ret += 1
        else:
            ret -= 1
    return ret

def sanity_test():
    x = 12
    n = 6
    assert(run(x, n) == 4)
    print("Sanity test args: x=", x, "n=", n)
    print("Sanity test passed")

def more_tests():
    tests = [
        [1,36,6],
        [1,36,7],
        [1,36,8],
        [3,36,9],
        [3,36,10],
        [3,36,11],
        [5,36,12]
    ]
    for test in tests:
        res, x, n = test
        #print("x=", x, "n=", n, "expected=", res, "got=", run(x, n))
        assert(run(x, n) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 74: Count values in multiplication tables')
    parser.add_argument('-x', help='Result of multiplication', type=int)
    parser.add_argument('-n', help='Max Multiplication table', type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.x and args.n:
        print("Result = ", run(args.k, args.n))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
