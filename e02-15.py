#!/usr/bin/env python

net_devices = {}

net_devices['ip_addr'] = '10.10.1.8'
net_devices['username'] = 'duncanb'
net_devices['password'] = 'ajablah'
net_devices['vendor'] = 'Cisco'
net_devices['model'] = '4948 10GE'

for k, v in net_devices.items():
    print k, v

net_devices['password'] = 'blahaja'
net_devices['secret'] = 'enabled!!'

_ = net_devices.get('os', 'cisco_ios')
print _

try:
    _ = net_devices['device_type']
except KeyError:
    _ = 'Err:  Device Type not available!!'

print _
