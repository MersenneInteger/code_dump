#!/usr/bin/python

#overloading the + operator
class SumList(object):
    
    def __init__(self, thisList):
        self.myList = thisList

    def __add__(self, other):
        newList = [x+y for x, y in zip(self.myList, other.myList)]
        return newList
    def __repr__(self):
        return str(self.myList)

oddList = SumList([1,3,5,7])
evenList = SumList([2,4,6,8])

newList = oddList + evenList
print(newList)

#inheriting from builtins
class MyDict(dict):
    def __setitem__(self, key, val):
        print("setting a key-value pair")
        dict.__setitem__(self, key, val)
dictionary = MyDict()
dictionary['A'] = 65
dictionary['B'] = 66
for key in dictionary.keys():
    print('{0}-{1}'.format(key, dictionary[key]))

#encapsulation
class GetSet(object):

    def __init__(self, value):
        self._attrval = value
    
    @property
    def var(self):
        print('getting "var" attribute')
        return self._attrval
    @var.setter
    def var(self, value):
        print('setting "var" attribute')
        self._attrval = value
    @var.deleter
    def var(self):
        print('deleting "var" attribute')
        self._attrval = None

ex = GetSet(5)
print(ex.var)
ex.var = 10
print(ex.var)
del ex.var
print(ex.var)

#with 

class MyClass(object):
    
    def __enter__(self):
        print('entering with')
        return self

    def __exit__(self, type, value, traceback):
        print('exiting with')
        print('Error Type: {0}, Value: {1}, Traceback: {2}'.format(type, value, traceback))
    def report(self):
        print('creating instance with {}'.format(id(self)))

with MyClass() as cc:
    cc.report()
    err = 5 / 0
print('exe after with block')

