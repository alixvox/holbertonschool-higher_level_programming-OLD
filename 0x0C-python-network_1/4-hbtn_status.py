#!/usr/bin/python3
""" This module fetches the status of a URL. """


if __name__ == '__main__':
    from requests import get

    req = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
