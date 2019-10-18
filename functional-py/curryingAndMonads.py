##Demystify Currying, Dispatching, and PyMonad

##functional composition and currying
#functional composition is the process of chaining 2+ functions together
#the output of one function serves as the input for the other
#f(g(x))

def comp_func(h_x, g_x):
    def final_func(*args, **kwargs):
        return h_x(g_x(*args, **kwargs))
    return final_func

import re

def add_suffix(string):
    return string + ' suffix'

def remove_punc(string):
    return re.sub(r'[^\w\s]', '', string)

composed_f = comp_func(remove_punc, add_suffix)
print(composed_f('hello? world!!'))

composed_f2 = comp_func(add_suffix, remove_punc)
print(composed_f2('hello? world!!'))

#currying
#transform function with multiple args to multiple single-arg higher order functions
#f(a,b,c,d) => f(a)(b)(c)(d)
from functools import partial

def some_func(a,b,c,d):
    return a * b + c - d

sf_f_b = partial(some_func, b=10)
sf_f_c = partial(sf_f_b, c=100)
sf_f_d = partial(sf_f_c, d=1)

print(sf_f_d(9))
print(some_func(9,10,100,1))

def predict_land_prices(yr_sold, yr_bought, init_price, area):
    return init_price + area * (yr_sold-yr_bought)*20 + 2000

plp_yr_bought = partial(predict_land_prices, yr_bought=2012)
plp_init_price = partial(plp_yr_bought, init_price=50000)
plp_area = partial(plp_init_price, area=1000)
print(plp_area(2022))
print(predict_land_prices(2022,2012,50000,1000))
print(plp_area(2030))

from inspect import signature

def curry_func(my_func):
    def inner_wrap(args):
        if len(signature(my_func).parameters) == 1:
            return my_func(args)
        else:
            return curry_func(partial(my_func, args))
    return inner_wrap

@curry_func
def do_some_ops(a,b,c,d):
    return a * b + c - d

print(do_some_ops(9)(10)(100)(1))

##functors
#functors are an object that can be treated as a function
#can be created by assigning functions to variables
#can be used for data hiding, method dispatching, etc

##single and multiple method dispatching
def func(a, b):
    return a + b

my_functor = func
print(my_functor(1,1))

class MyFunctor:
    def __call__(self, inp):
        if isinstance(inp[0], int):
            return self.add_2_int(inp)
        elif isinstance(inp[0], str):
            return self.add_2_str(inp)

    def add_2_int(self, inp):
        result = 0
        for x in inp:
            result += x
        return result
        
    def add_2_str(self, inp):
        result = ''
        for x in inp:
            result += x + ' '
        return result

class ExposedClass():
    def __init__(self):
        self.adder=MyFunctor()

    def add_stuff(self, my_list):
        return self.adder(my_list)

my_obj = ExposedClass()
print(my_obj.add_stuff(['hello', 'world']))
print(my_obj.add_stuff([1,2,3]))


#definition of functors can be extended to callable obects 
# like classes with call method implemented
from operator import mul

class MyOperationDoer:
    def __init__(self, init_val, op):
        self.op = op
        self.val = init_val

    def set_val(self, val):
        self.val = val

    def __call__(self, inp):
        result  = self.op(self.val, inp)
        self.val = result
        return result

my_obj = MyOperationDoer(10, mul)
print(my_obj(100))
print(my_obj(2))
my_obj.set_val(5)
print(my_obj(5))
my_obj.set_val(2)
print(my_obj(2))
print(my_obj(2))

##single - multiple method dispatching
#method dispatching - different implementations of same function depending on arg type

#dispatching using a dictionary
def add_2_ints(a, b):
    return a+b
def add_2_strs(a,b):
    return a+' '+b
def add_2_lists(a,b):
    return a+b

dispatch_dict = {
    (int,int): add_2_ints,
    (str,str): add_2_strs,
    (list,list): add_2_lists
}

def add_2_things(a,b):
    get_type_a = type(a)
    get_type_b = type(b)
    return dispatch_dict[(get_type_a, get_type_b)](a,b)

print(add_2_things(10,5))
print(add_2_things('hello', 'world'))
print(add_2_things([1,2], ['a','b']))

#single dispatching with functools
from functools import singledispatch
@singledispatch
def add_2_stuff(a,b):
    raise NotImplementedError('type not implemented')

@add_2_stuff.register(int)
def _(a,b):
    print('int')
    return a+b
@add_2_stuff.register(str)
def _(a,b):
    print('str')
    return a+' '+b

@add_2_stuff.register(list)
def _(a,b):
    print('list')
    return a+b

print(add_2_stuff(4,5))
print(add_2_stuff('hello','world'))
print(add_2_stuff([1,2], ['a','b']))

#stacking multiple single dispatches together
@add_2_stuff.register(int)
@add_2_stuff.register(float)
def _(a,b):
    print('int and/or float')
    return a+b

print(add_2_stuff(1.0, 1))
print(add_2_stuff(1.0, 2.0))

##monads
#monad - is a design pattern[1] that allows structuring programs
#  generically while automating away boilerplate code needed by the program logic
#Monads achieve this by providing their own data type, which represents 
# a specific form of computation, along with one procedure to wrap values of 
# any basic type within the monad (yielding a monadic value) and another to 
# compose functions that output monadic values (called monadic functions).

#more simply - its a type of object with special properties that works as a wrapper
#around the original object, allows imposition of an order on how an expression can be
#evaluated

#two types of values can be returned whan a funcition is applied on monads:
    #simple/normal values (Just values)
    #nothing/invalid (None, NaN)

#valid operations that can be performed on monads
    #unit operation: turns value into a monad
    #bind operation: transforms functions used to work on normal types into
        #into functions that can work on equivalent monad types

nothing = 'Nothing'
class Monad:
    def __init__(self, value):
        self.val = value
    def __repr__(self):
        return str(self.val)

class NothingValue(Monad):
    def __init__(self, value=nothing):
        self.val = nothing
    def bind(self, my_func):
        return self.val

class JustValue(Monad):
    def __init__(self, value):
        super().__init__(value)
    def bind(self, my_func):
        try:
            return JustValue(my_func(self.val))
        except:
            return NothingValue()

def add_2(x):
    return x+2

just_3 = JustValue(3)
print(just_3.bind(add_2))
just_str = JustValue('hello')
print(just_str.bind(add_2))
nothing_obj = NothingValue()
nothing_obj.bind(add_2)

print(just_3.bind(add_suffix))
print(just_str.bind(add_suffix))
print(nothing_obj.bind(add_suffix))

##pyMonad
#library with implementations of monads and related abstractions
#functional composition using (*) operator
#currying using @curry decorator
#partial functions and predefined monads
import pymonad

#currying with pymonad
from pymonad import curry

#def some_op(a,b,c,d):
#    return a+b-c*d

#print(some_op(1,2,3,4))

@curry
def some_op(a,b,c,d):
    return a+b-c*d

some_op_1 = some_op(1)
some_op_100 = some_op_1(100)
some_op_10 = some_op_100(10)
print(some_op_10(5))

#partially applying arguments
some_op(1)(100)(10)(5)

#functional composition using * operator
@curry
def remove_punctuation(string):
    return re.sub(r'[^\w\s]','', string)

@curry
def add_suffix_two(string):
    return string+' '+'suffix'

composed_fn = add_suffix_two * remove_punctuation
print(composed_fn('?h()e!!l#l@o w$o*r!@ld!!!?'))

#alternative currying methods
@curry
def partial_op1(x,y):
    return x+y

@curry
def partial_op2(x,y):
    return x-y

completed_op = partial_op1(10) * partial_op2(50)
print(completed_op(2))

completed_op_reverse = partial_op2(50) * partial_op1(10)
print(completed_op_reverse(2))

#using monads Just and Nothing
from pymonad import Just, Nothing


##updating docstrings with functools