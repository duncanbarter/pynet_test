#!/usr/bin/env python

def my_func(x, y, z=20):
    return x + y + z

test1 = my_func(1, 2, 3)
test2 = my_func(2, 3)
test3 = my_func(3, z=10, y=5)
test4 = my_func('i ', 'hate ', 'aol')
test5 = my_func([1, 5], [2, 6], [3, 7])

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

