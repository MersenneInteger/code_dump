#!/bin/python3

import os
import sys

def get_next_multiple(n):

    copy, count = n, 0
    while copy % 5 != 0:
        count += 1
        copy += 1
    if count < 3 and n >= 38:
        return n + count
    return n

def gradingStudents(grades):
    l = []
    for grade in grades:
        l.append(get_next_multiple(grade))
    return l

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)
    f.write('\n'.join(map(str, result)))
    f.write('\n')
    f.close()
