#!/usr/bin/env python

from pprint import pprint

import re
import subprocess

class NetDevice(object):
    def __init__(self, source):
        self.source = source
    
    def find_name(self):
        self.name = ''
        match = re.search(r"(.*?) uptime", self.source)
        if match:
            self.name = match.group(1)
    
    def find_vendor(self):
        self.vendor = ''
        match = re.search(r"(.*?) IOS Software", self.source)
        if match:
            self.vendor = match.group(1)
    
    def find_model(self):
        self.model = ''
        match = re.search(r"(.*?) processor", self.source)
        if match:
            self.model = match.group(1)
    
    def find_os(self):
        self.os = ''
        match = re.search(r"Cisco IOS Software, (.*)", self.source)
        if match:
            self.os = match.group(1)
    
    def find_serialno(self):
        self.serialno = ''
        match = re.search(r"Processor board ID (.*)", self.source)
        if match:
            self.serialno = match.group(1)
    
    def find_uptime(self):
        self.uptime = ''
        match = re.search(r"uptime is (.*)", self.source)
        if match:
            self.uptime = match.group(1)
    
    def populate(self):
        self.find_name()
        self.find_vendor()
        self.find_model()
        self.find_os()
        self.find_serialno()
        self.find_uptime()

    def __str__(self):
        _ = self.__dict__.copy()
        _.pop('source')
        output = '#####\n\n'
        for k, v in _.items():
            output = output + k + ': ' + v + '\n'
        output = output + '\n#####'
        return str(output)
    
def read_file(filename):
    with open(filename) as f:
        return f.read()

if __name__ == "__main__":

    switch = NetDevice(read_file('show_version.txt'))
    switch.populate()

    print(switch)
