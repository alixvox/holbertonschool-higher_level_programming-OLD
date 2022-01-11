#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_list = list(roman_string)
    numerals = [
        ('I', 1, None, None),
        ('V', 5, 'I', 1),
        ('X', 10, 'I', 1),
        ('L', 50, 'X', 10),
        ('C', 100, 'X', 10),
        ('D', 500, 'C', 100),
        ('M', 1000, None, None)]
    roman_list.reverse()
    number, idx = 0, 0
    for rom in numerals:
        if idx == len(roman_list):
            break
        while rom[0] == roman_list[idx]:
            number += rom[1]
            if idx == len(roman_list) - 1:
                idx += 1
                break
            if rom[2] == roman_list[idx + 1]:
                idx += 1
                number -= rom[3]
            idx += 1
            if idx == len(roman_list):
                break
    return number
