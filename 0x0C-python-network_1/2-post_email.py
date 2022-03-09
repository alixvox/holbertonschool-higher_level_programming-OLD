#!/usr/bin/python3
""" This module displays the response of a POST request
sent to a URL. """


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    email = {'email': argv[2]}
    source = urlencode(email).encode('utf-8')
    request = Request(argv[1], source)

    with urlopen(request) as url:
        print(url.read().decode('utf-8'))
