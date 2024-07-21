#!/usr/bin/python3

"""
a Python script that fetches the X-Request-Id header from a given URL
"""
import urllib.request
import sys
url = sys.argv[1]
response = urllib.request.Request(url)
try:
    with urllib.request.urlopen(response) as f:
        print(f.headers['X-Request-Id'])
except KeyError:
    print("Error: X-Request-Id not found")
