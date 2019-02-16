#!/bin/python3

import math, os, random, re, sys

def sockMerchant(n, ar):

    pairs = 0
    pairMap = {}

    for sock in ar:
        if sock in pairMap:
            pairs += 1
            del pairMap[sock]
        else:
            pairMap[sock] = sock
    return pairs

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input())
#    ar = list(map(int, input().rstrip().split()))
#    result = sockMerchant(n, ar)
#    fptr.write(str(result) + '\n')
#    fptr.close()
