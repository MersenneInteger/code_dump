#!/usr/bin/python
import math
import statistics
from functools import reduce

#map: apply function to items in list
def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]
areas = []
#direct method
for r in radii:
    a = area(r)
    areas.append(a)
#print(areas)

#using map
areas = list(map(area, radii))
print(areas)

#other map example
temps = [('Berlin', 29), ('Cario', 36), ('Tokyo', 27)]
cToF = lambda data: (data[0], (9/5)*data[1] + 32)
convertedList = list(map(cToF, temps))
print(convertedList)

#filter:
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
aboveAvg = list(filter(lambda x: x > avg, data))
print(aboveAvg)

#reduce
data = [2,3,5,7]
product = 1
for i in data:
    product *= i
print(product)

product = reduce(lambda x, y: x *y, data)
print(product)

