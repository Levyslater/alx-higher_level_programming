#!/usr/bin/python3

"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    main module
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print(f"    - type: {type(html)}")
    print(f"    - content: {html}")
    utf8_content = html.decode('utf-8')
    print(f"    - utf8 content: {utf8_content}")


if __name__ == "__main__":
    main()
