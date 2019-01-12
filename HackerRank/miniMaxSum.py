#!/bin/python3
import math, os, random, re, sys

def miniMaxSum(arr):

    mini, maxi = 0, 0
    arr.sort()
    for i in arr[:len(arr)-1]:
        mini += i
    for i in arr[1:len(arr)]:
        maxi += i
    print(f'{mini} {maxi}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
