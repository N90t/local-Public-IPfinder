#!/usr/bin/python3

import socket
from requests import get  #install request module

hostname =  socket.gethostname
localIP  = socket.gethostbyname(hostname)
publicIP = get('http://ifconfig.me')

#Here, we're using f-strings is to make string interpolation simpler.It's same way that you would with str.format()
print(f"Hostname: {hostname}")
print(f"Local_IP: {localIP}")
print(f'Public_IP: {publicIP}")
