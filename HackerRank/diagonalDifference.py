#!/bin/python3
import math, os, random,re, sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    
    lToR = 0
    rToL = 0
    for i in range(len(arr)):
        lToR += arr[i][i]
        rToL += arr[i][len(arr)-i-1]
    return abs(lToR-rToL)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
