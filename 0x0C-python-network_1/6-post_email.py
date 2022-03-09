#!/usr/bin/python3
"""  This module end a request to an email and prints
the response. """


if __name__ == '__main__':
    from requests import post
    from sys import argv
    email = {'email': argv[2]}
    req = post(argv[1], email)
    print(req.text)
