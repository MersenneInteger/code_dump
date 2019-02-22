#!/usr/bin/env python3
def swap_case(s):
    
    new_str = []
    for c in s:
        if not c.isalpha():
            new_str.append(c)
        elif ord(c) >= 97:
            new_str.append(chr(ord(c)-32))
        else:
            new_str.append(chr(ord(c)+32))
    return ''.join(new_str)

if __name__ == '__main__':
    #s = input()
    s = 'StRiNg.com//'
    result = swap_case(s)
    print(result)