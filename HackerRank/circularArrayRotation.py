#!/usr/bin/env python3

import math, os, random, re, sys

def circularArrayRotation(a, k, queries):

    for rotation in range(k):
        last = a[-1]
        del a[-1]
        a.insert(0, last)

    rotated = [a[q] for q in queries]
    return rotated

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)
    result = circularArrayRotation(a, k, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
