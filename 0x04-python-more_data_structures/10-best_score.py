#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    largest_key = max(a_dictionary, key=a_dictionary.get)
    return largest_key
