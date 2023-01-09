#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
    
    def def integer_validator(self, name, value):
        """validates a value as an integer
        """

        if type(value) != int:
            raise TypeError ("<name> must be an integer")
        elif value <= 0:
            raise ValueError ("<name> must be greater than 0")
