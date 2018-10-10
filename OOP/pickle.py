#!/usr/bin/python

import pickle
myList = ['a', 'b', 'c', 'd']
with open('pickleTest.txt', 'w') as fh:
    pickle.dump(myList, fh)

with open('pickleTest.txt') as fh:
    unpickledList = pickle.load(fh)
print(unpickledList)

n = 155
s = 'string'
dl = {'a': [1,2,3], 'b': [4,5,6]}
t = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]

with open('dataFile.txt', 'w') as fh:
    pickle.dump((n, s, dl, t), fh)
with open('dataFile.txt') as fh:
    tup = pickle.load(fh)
print(tup)

class MyClass(object):
    
    def __init__(self, n):
        self.n = n
    def get_val(self):
        return self.n

mc = MyClass(3)
with open('dataFile.txt', 'w') as fh:
    pickle.dump(mc, fh)
with open('dataFile.txt') as fh:
    unpickled_mc = pickle.load(fh)
print(unpickled_mc.get_val())
