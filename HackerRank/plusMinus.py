#!/bin/python3

import math, os, random, re, sys

def plusMinus(arr):
    pos, neg, zero = 0.0, 0.0, 0.0
    for i in arr:
        if i > 0: pos+=1.0
        elif i < 0: neg+=1.0
        else: zero +=1.0
    print(f'{pos/len(arr)}\n{neg/len(arr)}\n{zero/len(arr)}\n')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
