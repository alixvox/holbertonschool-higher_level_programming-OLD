#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_list = [char for char in roman_string]
    print(roman_list)
    number, idx = 0, 0
    for rom in roman_string:
        if rom == 'M':
            number = number + 1000
        elif rom == 'C':
            if roman_list[idx + 1] == 'D':
                number += 400
                idx += 1
            else:
                number += 100
        elif rom == 'D':
            if roman_list[idx - 1] == 'C' and idx != 0:
                continue
            else:
                number += 500
        elif rom == 'X':
            if roman_list[idx + 1] == 'L':
                number += 40
                idx += 1
            else:
                number += 10
        elif rom == 'L':
            if roman_list[idx - 1] == 'X' and idx != 0:
                continue
            else:
                number += 50
        elif rom == 'I':
            if roman_list[idx + 1] == 'V':
                number += 4
                idx += 1
            else:
                number += 1
        elif rom == 'V':
            if roman_list[idx - 1] == 'I' and idx != 0:
                continue
            else:
                number += 5
        idx += 1
    return number
