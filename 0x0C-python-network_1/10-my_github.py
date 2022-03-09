#!/usr/bin/python3
""" Displays Github id using the Github API. """


if __name__ == '__main__':
    from requests import get
    from requests.auth import HTTPBasicAuth
    from sys import argv
    reqs = get('https://api.github.com/user\
    ', auth=HTTPBasicAuth(argv[1], rgv[2])).json()
    print(reqs.get('id'))
