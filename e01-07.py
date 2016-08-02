#!/usr/bin/env python

your_ip = raw_input('I need your IP!  Be honest: ')
octets  = your_ip.split(".")

octets[-1] = '0'

bin_octets = [bin(int(x)) for x in octets(x)]

print('The octets of your IP are:\n{:12}{:12}{:12}{:12}\nSee, that wasn''t so scary!'.format(*octets))
print('And in binary!')
print('{}{}{}{}'.format(*bin_octets))
