#Implementing Utilities and Optimizing Storage

##composite design pattern
#creates tree-like hierarchical structures
#each component in a composite design may be a leaf node or a composite node

#three elements
    #component: defines basic properties of all elements in structure
    #leaf: bottom-most element, contains functionality offered by component class
    #composite: contains leaf nodes and/or composite nodes

class Component:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def print_name(self):
        print('Name of Employee: ' + self.name)

    def print_id(self):
        print('ID of Employee: ' + str(self.emp_id))

#composite node
class Manager(Component): #inherits from component
    def __init__(self, name, emp_id):
        super().__init__(name, emp_id)
        self.children = []
    
    def manages(self, emp):
        self.children.append(emp)

    def display_working_under(self):
        print('employees working under ' + self.name + ' are: ')
        for emp in self.children:
            print(emp.name)

#leaf node
class Employee(Component):
    def __init__(self, name, emp_id, operation):
        super().__init__(name, emp_id)
        self.operation = operation
    
    def display_operation(self):
        print(self.name + ' does the operation: ' + self.operation)

bobManager = Manager('Bob', 123)
emp1 = Employee('Bob', 55, 'Cooking')
emp2 = Employee('Sally', 44, 'Accounting')
bobManager.manages(emp1)
bobManager.manages(emp2)

bobManager.display_working_under()
emp1.display_operation()
emp2.display_operation()

bobManager.print_name()
bobManager.print_id()
emp1.print_name()
emp1.print_id()
emp2.print_name()
emp2.print_id()

##caching in python
#caching - store data in a temp container for later use
#storing data that is freq used speeds up execution

from functools import lru_cache

@lru_cache(maxsize=100)
def fibo_rec(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fibo_rec(n-1) + fibo_rec(n-2)

import time
n = 100
start_t = time.time()
result = fibo_rec(n)
end_t = time.time()
time_taken = end_t - start_t

print('time elapsed is ' + str(time_taken) + ' seconds')

##memoization in python
#technique for remembering results of function/method calls
#a cache for function calls

memo_cache = {}
def fib_memo(n):
    if n==0: return 0
    elif n==1: return 1
    else: 
        #check if value is already in cache
        if memo_cache.get(n, None):
            return memo_cache[n]
        result = fib_memo(n-1)+fib_memo(n-2)
        memo_cache[n] = result
        return result

n = 500
start_t = time.time()
result = fib_memo(n)
end_t = time.time()
time_taken = end_t - start_t

print('time elapsed: ', time_taken, ' seconds')

##operator module
import operator

print(operator.mul(5,6))
print(operator.sub(5,6))
print(operator.add(5,6))
print(operator.lt(5,6))

#passing higher order functions
my_list = [(1, 'hello'), (200, 'world'), (50, 'hi'), (179, 'bye')]
#sort according to first value in tuple
print(sorted(my_list, key=operator.itemgetter(0), reverse=True))
print(sorted(my_list, key=operator.itemgetter(0), reverse=False))

import timeit
from functools import reduce

timeit.timeit('reduce(lambda x, y: x * y, range(1,100))')
timeit.timeit('reduce(mul, range(1,100))', setup='from operator import mul')

