#!/bin/python3
import math, os, random, re, sys

def countingValleys(n, s):
    seaLevel, isValley, numOfValleys = 0, False, 0
    for step in s:
        if step == 'D': seaLevel -= 1
        elif step == 'U': seaLevel += 1
        if seaLevel == 0 and isValley:
            numOfValleys += 1
            isValley = False
        elif seaLevel < 0:
            isValley = True
    return numOfValleys
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
