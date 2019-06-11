#!/usr/bin/python3
""" Module for square inherited from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Ineheritance from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Magic function to print a representation in human language"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Function to return the size """
        return super().width

    @size.setter
    def size(self, value):
        """Handle the size"""
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def update(self, *args, **kwargs):
        """Function to update the values"""
        list_1 = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list_1[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Funtion to make a dictionary"""
        return ({'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y})
