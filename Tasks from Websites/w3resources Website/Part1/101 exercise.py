# 101. Write a Python program to access and print a URL's content to the console.

import requests
from http.client import HTTPConnection


conn = HTTPConnection("example.com")
conn.request("GET", "/")
result = conn.getresponse()
# retrieves the entire contents.
contents = result.read()
print(contents)


# data = requests.get('https://google.com/')
# print(data.text)
