#!/usr/bin/python3

"""
A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

import urllib
import sys


def main():
    """
    main module
    """
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL. Reason:", e.reason)
    except Exception as e:
        print("Error:", str(e))
