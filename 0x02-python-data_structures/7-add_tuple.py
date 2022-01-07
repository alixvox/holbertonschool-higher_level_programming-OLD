#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = (), 90
    if (len(tuple_a) < 2):
        if (len(tuple_a) < 1):
            a = (0, 0)
        else:
            a = (tuple_a[0], 0)
    else:
        a = tuple_a
    if (len(tuple_b) < 2):
        if (len(tuple_b) < 1):
            b = (0, 0)
        else:
            b = (tuple_b[0], 0)
    else:
        b = tuple_b
    new_tuple = (a[0] + b[0], a[1] + b[1])
    return new_tuple
