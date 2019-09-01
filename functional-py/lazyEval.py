## lazy evaluation

#nested functions

def outer_function(x):
    def inner_function(y):
        print('outer function: {0}'.format(x))
        print('inner function: {0}'.format(y))
    inner_function('world')

outer_function('hello ')

#inner functions have access to outer functions variables
#inner function can change outer variables within its own scope
#but the variable returns to the scope of the outer function
#after the inner function exits
def out(x):
    def inn(y):
        x = y
        print(x)
    inn(1)
    print(x)

out(5)

#nonlocal allows the inner function to change the outer functions variable
def out2(x):
    def inn2(y):
        nonlocal x
        x = y
        print(x)
    inn2(1)
    print(x)
    
out2(5)

##closure
#when a function can access a local variable from the outer function or enclosing scope
#that has finished executing
#three conditions:
        #must exist as a nested function
        #nested function must reference a value defined in the outer/enclosing function
        #outer function must return the inner function

def outer_func3(outer_var):
    def inner_func3():
        print(outer_var)
    return inner_func3

closure = outer_func3(5)
closure()

def add_two_cond(sen1, sen2):
    def use_op(my_op):
        print(sen1 + ' ' + my_op + ' ' + sen2)
    return use_op

op_closure = add_two_cond('work hard', 'play hard')
op_closure('and')
op_closure('or')

def raise_pow(pow_n):
    def raise_num(n):
        return n**pow_n
    return raise_num

my_pow = raise_pow(5)
print(my_pow(2))
print(my_pow(3))

##advanced lambdas

def add_two_nums(outer_x):
    return (lambda inner_x: outer_x + inner_x)
add_closure = add_two_nums(3)
print(add_closure(10))

def add_prefix(prefix_str):
    return (lambda my_str: prefix_str + ' ' + my_str)

add_hello = add_prefix('hello')
print(add_hello('john'))

x = 123
my_lambda = lambda a, i=x: a + i
print(my_lambda(10))
print(my_lambda(1))

#nested lambdas
multiplier = lambda n1: (lambda n2: n1 * n2)
multiply_5 = multiplier(5)
multiply_2 = multiplier(2)
print(multiply_2(5))
print(multiply_5(2))

#using import statements inside lambda
rand = (lambda rand_mod: rand_mod.choice(['a','b','c']))(__import__('random'))
print(rand)
print(rand)

#assign default values for unassigned keys in dictionary
import collections
my_dict = collections.defaultdict(lambda: 'key not assigned')
print(my_dict[3])

##lazy evaluation
#evaluation strategy to evaluate an expression only when its value is needed

#eager evaluation - evaluate expressions as they occur

def eager_func(a, b):
    a = a + b
    b = b - 10
    return a, b

def gen(a,b):
    a = a + 10
    b = b - 10
    yield a, b

eager = eager_func(9,10)
print(eager)

lazy = gen(9,10)
print(lazy) #returns a generator

print(next(lazy))

def eager_even():
    n = 0
    for i in range(0, 50):
        n += 2
        print(n)

def lazy_even():
    n = 0
    while n < 50:
        yield n
        n += 2

eager_even()
my_lazy_even = lazy_even()
print(next(my_lazy_even))
print(next(my_lazy_even))
print(next(my_lazy_even))
print(next(my_lazy_even))
print(next(my_lazy_even))
print(next(my_lazy_even))

