#!/bin/python3

import os
import sys

def timeConversion(s):
    hour, minute, sec, period = s[:2], s[3:5], s[6:8], s[8:10]
    if period == 'PM' and hour != '12': 
        hour = int(hour) + 12
    if hour == '12' and period == 'AM':
        hour = '00'
    return (f'{hour}:{minute}:{sec}')

if __name__ == '__main__':

    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
