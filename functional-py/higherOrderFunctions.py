##higher order functions
import itertools
import functools

#higher order functions take another function as an argument
# or return another function

def some_func(func_par, list_par):
    for elem in list_par:
        print(func_par(elem))
    return

my_list = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']
some_func(len, my_list)

def add_prefix(st):
    return 'prefix ' + st

some_func(add_prefix, my_list)


def hof(n):
    def multiple_5(x): return x * 5
    def multiple_3(x): return x * 3
    def multiple_2(x): return x * 2
    
    if n%5==0: return multiple_5
    elif n%3==0: return multiple_3
    else: return multiple_2

new_func = hof(5)
print(new_func(6))
print(new_func(5))

##map
#map takes a function and an iterable as parameters
#applies function to all elem's in the iterable
#and returns iterable of results

pokemon = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']
lengths = map(len, pokemon)
print(lengths)

print(list(map(lambda x: x * 2, pokemon)))

num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]

def square(x):
    return x**2
def cube(x):
    return x**3

diffs = list(map(lambda x, y: cube(y) - square(x), num1, num2))
print(diffs)

##filter
#takes a function and an iterable
#applies function to list and returns an iterator
#for which the functions returns true

num3 = num1 + num2
evens = list(filter(lambda x: x%2==0, num3))
odds = list(filter(lambda x:x%2!=0, num3))
print(evens)
print(odds)

result = filter(lambda x: len(x) > 5, pokemon)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

##iter
#create an iterator from an object and an optional sentinel (think EOF)
print('\niter\n')
pokemon = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']
pokeIter = iter(pokemon)
print(pokeIter)
print(type(pokeIter))

try:
    while True:
        print(next(pokeIter))
except Exception as e:
    print(e)

##itertools
#count(start,[step])
for i in itertools.count(2,3):
    if i>30:
        break
    else:
        print(i)

#cylce
#Make an iterator returning elements from the iterable and saving a copy of each. 
# When the iterable is exhausted, return elements from the saved copy. 
# Repeats indefinitely
i = 0
for poke in itertools.cycle(pokemon):
    if i > 10:
        break
    else:
        print(poke, end=' ')
    i += 1

#repeat
#Make an iterator that returns object over and over again.
#Runs indefinitely unless the times argument is specified.
for x in itertools.repeat(pokemon, 7):
    print(x)

#permutations
#Return successive r length permutations of elements in the iterable.
#basically returns all possible permutations of list in x sized tuples
for x in itertools.permutations(pokemon, 2):
    print(x)

for x in itertools.permutations([1,2,3,4,5], 2):
    print(x)

#combination
#Return r length subsequences of elements from the input iterable.
#retuns all combinations of list in
print('combination')
for x in itertools.combinations(pokemon,2):
    print(x)

#combination_with_replacement
#eturn r length subsequences of elements from the input iterable 
# allowing individual elements to be repeated more than once.
print('with replacement')
for x in itertools.combinations_with_replacement(pokemon,2):
    print(x)

#product
#returns cartesion products of list
print('product\n\n')
for x in itertools.product(pokemon, [1,2,3,4]):
    print(x)

#chain
#Make an iterator that returns elements from the first iterable until it is exhausted, 
# then proceeds to the next iterable, until all of the iterables are exhausted
print('\nchain\n\n')
for x in itertools.chain(pokemon, [1,2,3,4], "string"):
    print(x)

#starmap
#Make an iterator that computes the function using arguments obtained from the iterable
print('starmap')
for x in itertools.starmap(pow, [(1,2), (4,5), (5,6)]):
    print(x)

#zip
#zips two lists together in one list
for x in zip([1,2,3], ['a','b','c']):
    print(x)

#compress
#Make an iterator that filters elements from data returning only those that have 
# a corresponding element in selectors that evaluates to True. 
# Stops when either the data or selectors iterables has been exhausted.
for x in itertools.compress(pokemon, [1,True, None, 'hello']):
    print(x)

for x in itertools.compress([1,2,3,4,5], [True, True, True, True, True]):
    print(x)

#takewhile
#Make an iterator that returns elements from the iterable as
#  long as the predicate is true. Roughly equivalent to:
print('takewhile')
for x in itertools.takewhile(lambda x: x<3, [1,2,3,4,5]):
    print(x)

#dropwhile
#Make an iterator that drops elements from the iterable as long 
# as the predicate is true; afterwards, returns every element
print('dropwhile')
for x in itertools.dropwhile(lambda x: x<3, [1,2,3,4,5]):
    print(x)

##functools

#reduce
#reduce list to one value

print(functools.reduce(lambda x, y: x*y, [1,2,3,4,5]))
print(functools.reduce(lambda x, y: x + y, pokemon))

num4 = [1,2,3,4,5]
print(functools.reduce(lambda x,y: x*y, map(lambda x: x**2, num4)))

#sum of cubes
print(functools.reduce(lambda x,y: x+y, map(lambda x: x**3, num4)))

##decorators
#a decorator takes another function as input, modifies or adds functionality
#and returns the new function
#can be applied to any callable object like functions, methods, classes

def my_func():
    print('inside function')

def my_decorator(func):
    def wrapper_func():
        print('inside decorator')
        func()
        print('decorator finished')
    return wrapper_func

decorated_func = my_decorator(my_func)
decorated_func()

@my_decorator
def other_func():
    print('another function')

print('\n\n')
other_func()

#using arguments with decorators
print('\n\n')
def run_mult(n):
    def nested_decorator(my_func):
        def wrapper_run_mult():
            print('inside inner decorator')
            for i in range(0, n):
                my_func()
            print('inner decorator finished')
        return wrapper_run_mult
    return nested_decorator

@run_mult(n=5)
def another_func():
    print('more function')

another_func()
