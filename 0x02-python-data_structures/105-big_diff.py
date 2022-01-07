#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) == 0 or len(my_list) == 1:
        return 0
    a = my_list[0]
    b = my_list[0]
    for i in range(0, len(my_list)):
        if a < my_list[i]:
            a = my_list[i]
        if b > my_list[i]:
            b = my_list[i]
    return a - b
