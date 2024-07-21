#!/usr/bin/python3

"""
A Python script that fetches the X-Request-Id header from a given URL
"""

import urllib.request
import sys


def main():
    """
    main module
    """
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            headers = response.getheaders()
            x_request_id = dict(headers).get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("Error: X-Request-Id not found")
    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL. Reason:", e.reason)
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
