#!/usr/bin/python

import re

my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key = input('please input a key: ')
try:
    print('value for {0} = {1}'.format(key, my_dict[key]))
except KeyError:
    print('Exception thrown: key({0}) does not exist'.format(key))

class MyClass(object):
    
    @staticmethod
    def make_error():
        print('entering make_error')
        x = 5/0
        print('leaving make_error')

    def do_something(self):
        print('entering do_something')
        self.make_error()
        print('leaving do_something')

def some_util_func():
    print('entering some_util_func')
    cc = MyClass()
    cc.do_something()
    print('leaving some_util_func')

def some_major_func():
    print('entering some_major_func')
    some_util_func()
    print('leaving some_major_func')

def main():
    print('entering main')
    some_major_func()
    print('leaving main')
try:
    main()
except ZeroDivisionError as e:
    print('OOPS')
    print(e.args)

def process_date(date):
    
    if not re.search(r'\d\d\d\d-\d\d-\d\d$', date):
        raise ValueError('Please submit correct date format')
    else:
        print('date: {}'.format(date))

#process_date('1980-11-07')
#process_date('1-3-2018')

class CustomError(Exception):
    
    def __init__(self, *args):
        
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):

        if self.message:
            return 'Error thrown: {}',format(self.message)
        else:
            return 'Custom Exception thrown'

print()
#raise CustomError
raise CustomError('Wow an error')


