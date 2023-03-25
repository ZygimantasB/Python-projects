# 139. Write a Python program to valid a IP address.

import socket

hostname = socket.gethostname()
internal_ip_adress = socket.gethostbyname(hostname)

print(f"My internal host name: {internal_ip_adress}")

from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))

import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)

from requests import get

ip = get('https://api.ipify.org').text
print(f'My public IP address is: {ip}')