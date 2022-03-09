#!/usr/bin/python3
""" handles errors with request"""

import requests
import sys


def main():
    """handles errors with requests"""
    args = sys.argv
    url = args[1]
    try:
        r = requests.get(url)
        print(r.text)
    except r.status_code as e:
        print(e)
