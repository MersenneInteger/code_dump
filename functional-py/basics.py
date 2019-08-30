##functional programming

import itertools

##recursion
def factorial(n):
    
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

print(factorial(6))

def recuFactorial(n):

    if n <= 1:
        return n
    return  n * recuFactorial(n-1)

print(recuFactorial(6))

#fibonacci - iterative
def fib(n):

    j = 0
    k = 1
    for _ in range(1, n+1):
        l = j + k
        k = j
        j = l
    return l

#0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765
print(fib(8))
print(fib(9))
print(fib(11))

def printFib(n):
    num1 = 0
    num2 = 1
    count = 2
    if  n == 0:
        return
    elif n == 1:
        print(num1)
    elif n >= 2:
        print(num1, num2, end=' ')
    
    while count <= n:
        num3 = num1 + num2
        print(num3, end=' ')
        count += 1
        num1 = num2
        num2 = num3
    return

printFib(13)
print()
#fibonacci - recursive
def recFib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)

for i in range(0,20):
        print(recFib(i), end=' ')
print()

##immutability and mutability
x = 123
y = 123
#both will have the same unique id
print(id(x))
print(id(y))

x += 1
print(id(x))
print(id(y))

#lists are mutable
zList = [1,2,3]
print(id(zList))
zList.append(4)
print(id(zList))

#immutable datatypes
    #integer, float, byte, string, double, range, complex, bool, frozenset
#mutable datatypes
    #list, dictionary, set, byte array, user defined classes

##first-class functions

#functions can be passed as parameters to other functions, assigned to variables, 
# can be used as a return type and stored in data structures
my_var = 3
def my_func(var_x):
    var_result = var_x + 3
    return var_result

new_var = my_func(my_var)
print(new_var)

#likewise with functions
def square(x):
    return x * x
    
def func(x, function):
    result = function(x)
    return result

new_var = func(6, square)
print(new_var)

#assigning functions to variables
var = 3
new_var = var
print(new_var)

sq = square
print(sq(5))

#using functions as return types to functions
my_var = 3
def func2(x):
    ret_x = x + 2
    return ret_x
my_new_var = func2(my_var)
print(my_new_var)

def square_something(x):
    def func_square(y,z):
        return y * y + z
    return func_square(x, x+1)

my_new_var = square_something(5)
print(my_new_var)

#can be stored in data structures
def sqr(x):
    return x * x
def cube(x):
    return x * x * x
def four_pow(x):
    return x * x * x * x

func_list = [sqr, cube, four_pow]
for func in func_list:
    print(func(2))

##lambda expressions

#lambda expressions are anonymous functions that are typically used once
square = lambda x: x * x
print(square(5))

list_str = ['dddd', 'a', 'ccc', 'bb']
print(sorted(list_str, key = lambda x: len(x)))

dict_str = {1: 'a', -2: 'bbbb', 3:'c', 4:'ddddd'}
print(sorted(dict_str, key=lambda x: len(dict_str[x])))

##classes, objects and functions

#keyword args - default parameters
def optArg(x=1):
    return x
xx = optArg()
print(xx)

#assign to specific parameters
def specArg(x, y, z):
    return x + y + z
xx = specArg(x=1, z=3, y=2)
print(xx)

#variable arguments
def varArg(*args):
    for arg in args:
        print(arg, end=' ')

varArg(1)
varArg(2,3,4,5, )
print()
varArg('a', 'b', 'c')
print()

#variable keyword arguments
def keyArg(**kwargs):
    for key in kwargs:
        print('Arg: ', key, ' is: ', kwargs[key], end=' ')

keyArg(arg1=1)
print()
keyArg(arg1=2,arg2=3,ar3=4,arg4=5)
print()
keyArg(a='a', b='b', c='c')
print()

##lists and tuples
list1 = [1,2,3, 'a', 'b', 'c', True, 3.0]
for elem in list1:
    print(elem, end=' ')

print()
print(list1[1:]) #print everything past the first element

print(list1[2:5])
print(list1[-1]) #print last elem
print('second to last: ' + str(list1[-2]))

if True in list1:
    print('True is in list')

#tuples are immutable lists
tup1 = (1,2,3,4,5)
for tup in tup1:
    print(tup)

#error
#tup1[1] = 6
#tup1.addend(6)

##dictionaries and sets
#sets are ordered collections and are mmutable
print()
set1 = {1,2,3,'a','b','c'}
set2 = set({7,8,9})

#sets dont support indexing
#set1[1] #error

def printSet(set):
    for s in set:
        print(s, end=' ')

set1.add(5)
printSet(set1)
#all elements must be unique
set1.add(5)
print()
printSet(set1)

set1.update(set2)
print()
printSet(set1)

set1.add(0)
printSet(set1)

#set operations
set3 = {1,2,3,4,5}
set4 = {1,3,5,7,9}
set5 = {2,4,6,8,10}
set6 = {1,2,3}
set7 = {}

print()
print(set3 | set4) # '|' - union
print(set3 & set4) # '&' - intersect
print(set3 - set4) # '-' - difference
print(set3 > set4) # '>' - superset
print(set3 > set6)

#two sets are disjoint if they have no elements in common
print(set3.isdisjoint(set4))
print(set3.isdisjoint(set7))

setList = [set1, set2, set3, set4, set5, set6, set7]
for s in setList:
    s.clear()

#dictionaries store data in key-value pairs
#keys are immutable but dictionaries themselves are mutable

dict1 = {'a':1, 'b':2, 'c':3}
print(dict1)
print(dict1['b'])
del dict1['c']
print(dict1)

#get - gets a value or a default value if the key is not present
print(dict1.get('d', None))
print(dict1.get('a', None))

for kvp in dict1.items():
    print(kvp)
for (k,v) in dict1.items():
    print('key: {0}\nvalue: {1}'.format(k,v))

##generators and yield
#generators create iterators using yield
def gen(a,b):
    yield a, b
    print('first')
    a+=1
    b+=2
    yield a, b
    print('second')
    a+=10
    b+=20
    yield a, b
    print('third')

genEx = gen(3,7)
for x, y in genEx:
    print(x, y)

##list and dictionary comprehension
#creates a list based on an iterable
#syntax:
#   resulting_list = [expression for item in iterable]

nums = [1,2,3]
numsTimesTwo = [x * 2 for x in nums]
print(nums)
print(numsTimesTwo)

evens = [x for x in range(1,11) if x%2==0]
odds = [x for x in range(1,11) if x%2!=0]
print(evens)
print(odds)

strList = ['string', 'another string', 'str', 's']
strLenList = [len(x) for x in strList]
print(strLenList)

nums2 = [11,14,8,15,4,3,77,21,6]
numsOverTen = list(filter(lambda x: x > 10, nums2))
print(numsOverTen)

#dictionary comprehensions
#syntax:
#   resulting_variable = {key: value for (key, value) in iterable}
list99 = [1,2,3,4,5,6,7,8,9]
list100 = {elem: elem**2 for elem in list99}
print(list100)

evenSquares = {elem: elem**2 for elem in list99 if elem%2==0}
print(evenSquares)

listA = [1,2,3]
listB = ['a','b','c']
dictA = {key: value for (key, value) in zip(listA, listB)}
print(dictA)