#!/bin/python3

import math, os, random, re, sys

def compareTriplets(a, b):

    score1 = 0
    score2 = 0
    for x,y in zip(a, b):
        if x > y: score1 += 1
        elif x < y: score2 += 1
    return score1, score2

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
