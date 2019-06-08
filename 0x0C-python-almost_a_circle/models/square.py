#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def update(self, *args, **kwargs):
        list_1 = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list_1[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return super().to_dictionary()

    def to_dictionary(self):
        return ({'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y})
