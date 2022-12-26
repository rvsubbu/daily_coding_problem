#!/usr/bin/env python3

# This problem was asked by Facebook.

# Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

import argparse

def run(k, nums):
    '''
    sum up k "best" subsequencs of all increasing subsequences
    keyword args:
    k -- number of subsequences to sum up
    nums -- sequence of nums
    '''
    if not nums:
        return 0

    sales = []
    start = None
    prev = nums[0]

    #import pdb; pdb.set_trace()
    for i, curr in enumerate(nums[1:]):
        if start == None and prev < curr:  # if nums[0] < nums[1], init a transaction
            start = prev

        if curr < prev:
            if start != None and prev > start:
                sales.append(prev-start)
            start = curr
        elif i == len(nums)-2: # end of nums
            if start != None:
                sales.append(curr-start)

        prev = curr

    #print("sales=", sales)
    if len(sales) > k:
        sales = sorted(sales)
        sales = sales[-k:]

    ret = 0
    for sale in sales:
        ret += sale
    return ret

def sanity_test():
    k = 2
    nums = [5,2,4,0,1]
    assert(run(k, nums) == 3)
    print("Sanity test passed")
    print("Sanity test args: k=", k, "nums=", nums)
    print("Sanity test result: 3")

def more_tests():
    tests = [
        ( 0, 2, [1]),
        ( 0, 2, [1,1]),
        ( 1, 2, [1,1,2]),
        ( 1, 2, [1,1,1,2]),
        ( 2, 2, [1,2,2,3]),
        ( 2, 2, [1,2,2,2,3]),
        ( 3, 2, [1,1,2,2,3,2,3]),
        ( 5, 2, [1,1,2,2,3,2,3,4,5]),
        (12, 2, [1,1,2,2,3,2,3,4,5,1,10]),
        ( 2, 2, [1,1,2,3]),
        ( 1, 2, [1,2]),
        ( 2, 2, [1,2,3]),
        ( 3, 2, [1,2,3,4]),
        ( 3, 2, [1,2,4,3]),
        ( 4, 2, [1,4,2,3]),
        ( 0, 2, [2,1]),
        ( 2, 2, [2,1,2,3]),
        ( 4, 2, [2,1,2,5]),
        ( 2, 2, [2,1,3]),
        ( 0, 2, [4,3,2,1]),
        ( 5, 2, [1,4,3,2,4]),
        ( 3, 3, [1,1,2,2,3,2,3]),
        ( 5, 3, [1,1,2,2,3,2,3,4,5]),
        (14, 3, [1,1,2,2,3,2,3,4,5,1,10])
    ]
    for test in tests:
        res, k, nums = test
        #print("k=", k, "nums=", nums, "expected=", res, "got=", run(k, nums))
        assert(run(k, nums) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 866: Find max profitable stock sales')
    parser.add_argument('-k', help='Number of sales transactions', type=int)
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
