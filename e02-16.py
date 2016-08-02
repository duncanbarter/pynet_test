#!/usr/bin/env python

def _readfile(filename):
    with open(filename) as f:
        return f.read().splitlines()

def _findserial(data):
    for line in data:
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID ")
            return serial_number

switch_output = _readfile('show_version.txt')
switch_serial = _findserial(switch_output)

print "\nSerial Number is {}\n".format(switch_serial)
