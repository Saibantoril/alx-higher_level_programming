#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Division = a/b
    except ZeroDivisionError:
        Division = None
    finally:
        print("Inside result:{}".format(Division))
    return (Division)
