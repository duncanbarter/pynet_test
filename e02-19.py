#!/usr/bin/env python
from pprint import pprint

def _readfile(filename):
    with open(filename) as f:
        return f.read()

def _findname(data):
    for line in data.splitlines():
        if 'uptime' in line:
            name, _ = line.split(' uptime')
            return name
    return ''

def _findvendor(data):
    for line in data.splitlines():
        if 'Cisco IOS Software' in line:
            return 'Cisco'
    return ''

def _findmodel(data):
    for line in data.splitlines():
        if 'processor' in line:
            model, _ = line.split(' processor')
            return model
    return ''

def _findos(data):
    for line in data.splitlines():
        if 'Cisco IOS Software' in line:
            _, os = line.split('IOS Software, ')
            return os
    return ''

def _finduptime(data):
    for line in data.splitlines():
        if 'uptime' in line:
            _, uptime = line.split('uptime is ')
            return uptime
    return ''

def _findserial(data):
    for line in data.splitlines():
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID ")
            return serial_number
    return ''

switch = {}
switch_output = _readfile('show_version.txt')
switch['name']   = _findname(switch_output)
switch['vendor'] = _findvendor(switch_output)
switch['model']  = _findmodel(switch_output)
switch['os']     = _findos(switch_output)
switch['uptime'] = _finduptime(switch_output)
switch['serial'] = _findserial(switch_output)

pprint(switch)
