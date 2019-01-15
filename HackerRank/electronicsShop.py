#!/bin/python3
import os, sys

def getMoneySpent(keyboards, drives, b):

    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    maxi = -1

    for keyboard in keyboards:
        for drive in drives:
            if (keyboard + drive) <= b and maxi < (keyboard + drive):
                maxi = keyboard + drive
    return maxi

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
