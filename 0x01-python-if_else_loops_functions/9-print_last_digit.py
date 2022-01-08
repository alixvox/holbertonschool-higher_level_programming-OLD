#!/usr/bin/python3
def print_last_digit(number):
    abs_num = abs(number)
    last_dig = abs_num % 10
    print("{:d}".format(last_dig), end='')
    return last_dig
