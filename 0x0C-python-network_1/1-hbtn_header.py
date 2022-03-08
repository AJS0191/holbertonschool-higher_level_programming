#!/usr/bin/python3
"""fetches a urls x-request-id"""

import urllib.request
import sys


def main():
    """fetches a urls x-request-id"""
    args = sys.argv
    with urllib.request.urlopen(args[1]) as response:
        result = response.read()
        varDic = response.info()
        for key, value in varDic.items():
            if key == 'X-Request-Id':
                print(value)


if __name__ == "__main__":
    main()
