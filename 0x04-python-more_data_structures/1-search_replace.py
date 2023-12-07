#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [item if type(item) is not list else item[:]
                for item in my_list]
    ac = len(my_list)
    for i in range(ac):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
