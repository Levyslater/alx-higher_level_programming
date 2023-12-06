#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list i6s None or len(my_list) < 1:
        return
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
