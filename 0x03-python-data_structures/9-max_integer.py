#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = [item if type(item) is not list else item[:]
                for item in my_list]
    i = len(new_list) - 1
    while i > 0:
        j = 0
        while j < i:
            if new_list[j] > new_list[j + 1]:
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp
            j += 1
        i -= 1
    return new_list[-1]
