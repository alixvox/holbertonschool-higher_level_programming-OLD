#!/usr/bin/python3
""" This module displays the response from sending to a URL. """


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    request = Request(argv[1])
    try:
        with urlopen(request) as url:
            url = url.read()
            print(url.decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
