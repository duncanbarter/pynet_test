#!/usr/bin/env python

with open('testfile') as f:
    f_lines = f.read()

print(f_lines)

with open('staticfile', 'w') as f:
    f_lines = 'This is a test file.\nIt is crudely formatted as a single string.\nBut it should print nicely.'
    f.write(f_lines)

with open('staticfile') as f:
    f_check = f.read()

print(f_check)

with open('testfile', 'a') as f:
    f.write(f_check)

with open('testfile') as f:
    f_appended = f.read()

print(f_appended)
