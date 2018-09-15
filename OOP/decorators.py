#!usr/bin/python

#class and static methods (ie not bound to an instance)
class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterInt(val)
        InstanceCounter.count += 1
    def setVal(self, val):
        self.val = val
    def getVal(self):
        return self.val
    
    #is neither a class method or a bound-instance method, just a utility
    #notice we are using the instance to call it but are not passing the instance
    @staticmethod
    def filterInt(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    #unbound method, can be called from class itself, unbound to any particular instance
    @classmethod
    def getCount(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(1)
c = InstanceCounter(9)

print(InstanceCounter.getCount())

#abstract classes

import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def setVal(self, val):
        '''set a value in the instance'''
        return
    @abc.abstractmethod
    def getVal(self):
        '''get and return a value from the instance'''
        return

class myClass(GetterSetter):
    
    def setVal(self, val):
        self.val = val
    def getVal(self):
        return self.val

x = myClass
print(x)

