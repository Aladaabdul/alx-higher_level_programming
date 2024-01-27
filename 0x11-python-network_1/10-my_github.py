#!/usr/bin/python3
"""Access github

"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
