#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary.values())[0]
    for key, val in a_dictionary.items():
        if val > max:
            max = val
            win_key = key
    return win_key
