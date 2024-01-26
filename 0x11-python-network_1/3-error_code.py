#!/usr/bin/python3
"""Manage Error

"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
