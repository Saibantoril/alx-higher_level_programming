#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        sorted_list = my_list.sort(reverse = True)
        max_int = sorted_list[0]
        return (max_int)
