#!usr/bin/python
import random

class Date(object):
    def getDate(self):
        return '09-02-18'

#time inherits Date
class Time(Date):
    def getTime(self):
        return '07-07-07'

dt = Date()
print(dt.getDate())

tm = Time()
print(tm.getTime())
print(tm.getDate())

#object.attribute lookup hierachy
#1)the instance
#2)the class
#3)any class from which this class inherits

class Animal(object):

    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print('{0} is eating {1}'.format(self.name, food))

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def bark(self):
        print('{} barked!'.format(self.name))

class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.breed = random.choice(['Tabby', 'Mutt'])

    def meow(self):
        print('{} meowed!'.format(self.name))

class GuardDog(Dog):
    
    def __init__(self, name):
        super(Dog, self).__init__(name)
        print('{} is a guard dog'.format(self.name))

benji = Dog('Benji')
garfield = Cat('Garfield')
benji.eat('kibble')
garfield.eat('birds')
benji.bark()
garfield.meow()
#garfield.bark() #error
print(benji.breed)
print(garfield.breed)

#for multiple inheritance, the method resolution order is depth-first then breadth
fido = GuardDog('Fido')
fido.eat('dog food')
fido.bark()
print('GuardDog class method resolution order: {}'.format(GuardDog.mro()))
print()

class A(object):
    def doThis(self):
        print('doing this in A')
class B(A):
    pass
class C(A):
    def doThis(self):
        print('doing this in C')
class D(B, C):
    pass

d = D()
d.doThis()
print(D.mro())

