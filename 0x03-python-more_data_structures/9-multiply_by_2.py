#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dictionary = {}
    for key, val in a_dictionary.items():
        mul_dictionary[key] = val*2
    return mul_dictionary
