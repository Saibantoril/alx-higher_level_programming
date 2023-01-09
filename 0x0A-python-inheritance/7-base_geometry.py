#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
    
    def def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError ("<name> must be an integer")
        elif value <= 0:
            raise ValueError ("<name> must be greater than 0")
