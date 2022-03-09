#!/usr/bin/python3
""" This module displays the X-Request-Id variable found in
the header of the response sent from a URL. """


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    with urllib.request.urlopen(sys.argv[1]) as url:
        html = url.info()
        print('{}'.format(html.get('X-Request-ID')))
