#!/usr/bin/env python3

# This problem was asked by LinkedIn.

# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].


import argparse
from collections import Counter

def run(points, center, k):
    '''
    Given a central point and list of points, return k nearest points
    '''
    if not points:
        return 0

    dists = {}
    for point in points:
        xdist = point[0]-center[0]
        ydist = point[1]-center[1]
        dists[point] = xdist*xdist + ydist*ydist
    sorted_by_dist = {k: v for k,v in sorted(dists.items(), key=lambda item: item[1])}
    return list(sorted_by_dist.keys())[:k]

def sanity_test():
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
    points = [(0,0), (5,4), (3,1)]
    center = (1,2)
    k = 2
    res = run(points, center, k)
    assert(res[0]==(0,0))
    assert(res[1]==(3,1))
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

def coords(s):
    try:
        x,y = map(int, [n.strip() for n in s.split(',')])
        return x,y
    except:
        raise argparse.ArgumentTypeError("Coordinates must be x,y")

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 888: Given a central point and list of points, return k nearest points')
    parser.add_argument('-p', '--points', help='List of Points', type=coords, nargs="+")
    parser.add_argument('-c', '--center', help="Central point", type=coords)
    parser.add_argument('-k', help="nearest <k> points", type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.points and args.center and args.k:
        print("Result = ", run(args.points, args.center, args.k))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
