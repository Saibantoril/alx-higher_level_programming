#!/usr/bin/python3
"""This module inherits from the list class"""

class Mylist(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
