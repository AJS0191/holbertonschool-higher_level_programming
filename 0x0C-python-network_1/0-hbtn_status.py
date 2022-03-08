#!/usr/bin/python3
"""fetches a url and displays"""

import urllib.request


def main():
    """fetches a url and displays"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        result = response.read()
    print("Body response:")
    print(f"    - type: {type(result)}")
    print(f"    - content: {result}")
    print(f"    - utf8 content: {result.decode('utf-8')}")


if __name__ == "__main__":
    main()
