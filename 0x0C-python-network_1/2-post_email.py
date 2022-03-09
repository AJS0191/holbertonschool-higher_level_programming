#!/usr/bin/python3
"""passes an email to a url"""

import urllib.request
import urllib.parse
import sys


def main():
    """passes an email to a url"""
    args = sys.argv
    url = args[1]
    email = args[2]
    values = {}
    values['email'] = email
    data = urllib.parse.urlencode(values)
    data = data.encode(encoding='utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
    print(result)


if __name__ == "__main__":
    main()
