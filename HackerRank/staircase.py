#!/bin/python3

import math, os, random, re, sys

def staircase(n):
    for i in range(1,n+1):
        j = n-i-1
        if(j >= 0):
            print(" " * (j), "#" * (i))
        else:
            print("#" * (i))

if __name__ == '__main__':
    n = int(input())
    staircase(n)