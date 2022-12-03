#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if type(i) is int:
            print("{}".format(i))
        elif type(i) is str:
            try:
                print("{:d}".format(i))
            except TypeError:
                print("The value {} cannot be converted \
                        into integer.".format(i))
