#!/usr/bin/python3
def islower(c):
    if ord(c) < 97 or ord(c) > 122 or not c:
        return False
    else:
        return True
