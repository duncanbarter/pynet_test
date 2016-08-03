#!/usr/bin/env python

from netmiko import ConnectHandler

def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def main():
    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':          '184.105.247.70',
        'username':    'pyclass',
        'password':    '88newclass',
    }

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':          '184.105.247.72',
        'username':    'admin1',
        'password':    '99saturday',
    }

    for curr_device in (pynet_rtr1, pynet_sw1):
        sw_con = ConnectHandler(**curr_device)

        show_ver = sw_con.send_command("show version")
        show_run = sw_con.send_command("show run")

        save_file(sw_con.base_prompt + '-ver', show_ver)
        save_file(sw_con.base_prompt + '-run', show_run)

if __name__ == "__main__":
    main()
