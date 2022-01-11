#!/usr/bin/python3
def roman_to_int(roman_string):
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



    """
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
        """
    return number
