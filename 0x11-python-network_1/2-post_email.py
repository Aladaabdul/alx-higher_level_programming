#!/usr/bin/python3
"""sends a POST request to the passed URL 
    with the email as a parameter
    and displays the body of the response
"""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Your email is: {}".format(body))
