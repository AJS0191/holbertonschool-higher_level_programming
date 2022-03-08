#!/usr/bin/python3
"""fetches a url and displays"""

import urllib.request


def main():
    """fetches a url and displays"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        result = response.read()
    print("Body response:")
    print("    - type: {}".format(type(result)))
    print("    - content: {}".format(result))
    print("    - utf8 content: {}".format(result.decode('utf-8')))


if __name__ == "__main__":
    main()
