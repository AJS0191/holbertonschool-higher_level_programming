#!/usr/bin/python3

import requests


def main():
    """sending a request to holberton intranet"""
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.encoding)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
