#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        self.__width = width
        return width
    
    @width.setter
    def width(self, value):
        if type(width)!= int:
            raise TypeError ("width must be an integer")
        elif width < 0:
            raise ValueError ("width must be >= 0")
        self.__width = value
    @property
    def height(Self):
        self.__height = height
        return height

    @height.setter
    def height(self, value):
        if type(height)!= int:
            raise TypeError ("height must be an integer")
        elif height < 0:
            raise ValueError ("height must be >= 0")
        self.__height = value

    

        



