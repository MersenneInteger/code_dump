#apple and orange

#!/bin/python3
import math, os, random, re, sys

def countApplesAndOranges(s, t, a, b, apples, oranges):

    #apps, orgs = 0, 0
    #for apple in apples:
    #    if a + apple in range(s,t+1):
    #        apps += 1
    #for orange in oranges:
    #    if b + orange in range(s,t+1):
    #        orgs += 1
    ap = [x+a for x in apples if x+a in range(s,t+1)]
    ora = [x+b for x in oranges if x+b in range(s,t+1)]
    print(len(ap))
    print(len(ora))

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
    


