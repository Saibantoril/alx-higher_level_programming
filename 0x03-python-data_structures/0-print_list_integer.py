#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if type(i) is int:
            print("{:d} is an integer." .format(i))