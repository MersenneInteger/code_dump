#!/usr/bin/python

x = 1
y = 's'
z = []
print(type(x), type(y), type(z))
#there are no primative types, everything is an object
#print(dir(x))

#class: blueprint for an instance
#instance: a constructed object of the class
#type: indicates the class the instance belongs to
#attribute: any object value
#method: a callable attribute defined in the class

class myClass(object):

    def __init__(self, val=10):
        self.var = int(val)

    def changeVar(self, val):
        try:
            self.var = int(val)
        except ValueError:
            print('type error in {}'.format(self))
            return

    def printVar(self):
        print(self.var)

myObject = myClass()
otherObject = myClass()
print(type(myObject))
print(myObject, otherObject)
print(myObject.var)

myObject.changeVar(5)
print(myObject.var)
myObject.printVar()
otherObject.printVar()
otherObject.changeVar('error')

thirdObject = myClass(42)
thirdObject.printVar()
