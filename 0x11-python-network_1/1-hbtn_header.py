#!/usr/bin/python3
"""Python script that takes in a URL
    sends a request to the URL
    and displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)