#!/usr/bin/env python

your_ip = raw_input('I need your IP!  Be honest: ')
octets  = your_ip.split(".")

print('The octets of your IP are:\n{:12}{:12}{:12}{:12}\nSee, that wasn''t so scary!'.format(*octets))

