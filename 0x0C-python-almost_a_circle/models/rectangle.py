#!/usr/bin/python3
"""Module for Rectangle inherited from base """
from models.base import Base


class Rectangle(Base):
    """Ineheritance from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """funtion that return the width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Private function for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Function that return the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Private funcction to handle the value of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Function to return the X axis """
        return self.__x

    @x.setter
    def x(self, value):
        """Handle X axis """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Function to return the Y axis """
        return self.__y

    @y.setter
    def y(self, value):
        """Handle Y axis """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Function to return the area"""
        return self.height * self.width

    def display(self):
        """Print the rectangle with # """
        if self.__width == 0 or self.__height == 0:
            print()
        for a in range(self.y):
            print()
        for a in range(self.height):
            print(" " * self.x, end='')
            for b in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """Magic function to print a representation in human language"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Function to update the values"""
        list_1 = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list_1[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Funtion to make a dictionary"""
        return ({'id': self.id, 'width': self.width,
                 'height': self.height, 'x': self.x, 'y': self.y})
