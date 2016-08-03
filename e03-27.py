#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

import sys

def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def main():
    rtr1_pass = getpass("Enter router password: ")
    sw1_pass  = getpass("Enter switch password: ")

    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':          '184.105.247.70',
        'username':    'pyclass',
        'password':    rtr1_pass,
    }

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':          '184.105.247.72',
        'username':    'admin1',
        'password':    sw1_pass,
    }

    sw_con = ConnectHandler(**pynet_rtr1)

    config_commands = ['vlan 808', 'name sk1tools',]

    output_embedded = sw_con.send_config_set(config_commands)
    output_imported = sw_con.send_config_from_file(sw_con.base_prompt + '-config-updates')

    print '#' * 60
    print 'EMBEDDED COMMAND RESULTS\n'
    print output_embedded
    print '\n'

    print '#' * 60
    print 'IMPORTED COMMAND RESULTS\n'
    print output_imported
    print '\n'

    print '#' * 60
    print 'FINAL VLAN OUTPUT\n'
    print sw_con.send_command('show vlan')
    print '\n'

if __name__ == "__main__":
    main()
