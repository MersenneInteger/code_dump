#!/bin/python3
import math, os, random, re, sys

def birthdayCakeCandles(ar):

    maxi, freq = ar[0], 0
    #maxi = max([x for x in ar])
    #freq = [x for x in ar if x == maxi]
    #return len(freq)

    #without built-ins
    for i in range(len(ar)-1):
        if ar[i] < ar[i+1]:
            maxi = ar[i+1]
    for i in ar:
        if i == maxi:
            freq += 1
    return freq

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
