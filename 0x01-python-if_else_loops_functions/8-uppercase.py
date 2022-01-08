#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str) - 1):
        is_lower = ord(str[i]) > 96 and ord(str[i]) < 123
        print(chr(ord(str[i]) - 32) if is_lower else str[i], end='')
    i += 1
    is_lower = ord(str[i]) > 96 and ord(str[i]) < 123
    print(chr(ord(str[i]) - 32) if is_lower else str[i])
