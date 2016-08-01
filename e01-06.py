#!/usr/bin/env python

a, b = raw_input('Please enter two numbers: ').split()

a = int(a)
b = int(b)

print('For A and B:\nsum = {:d}\ndifference = {:d}\nproduct = {:d}\nquotient = {:f}'.format(a + b, a - b, a * b, a / float(b)))

