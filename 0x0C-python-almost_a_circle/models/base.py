#!/usr/bin/python3
import json
import csv


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lista = []
        if list_objs is not None:
            for a in list_objs:
                lista.append(a.to_dictionary())

        with open("{}.json".format(cls.__name__), 'w',
                  encoding="UTF8") as myfile:
            myfile.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            replica = cls(1, 1)
        elif cls.__name__ == 'Square':
            replica = cls(1)
        replica.update(**dictionary)
        return replica

    @classmethod
    def load_from_file(cls):
        listo = []
        try:
            with open(cls.__name__ + '.json', 'r') as myfile:
                arch = cls.from_json_string(myfile.read())
                for a in arch:
                    listo.append(cls.create(**a))
        except:
            pass
        return listo

    @classmethod
    def save_to_file_csv(cls, list_objs):
        for a in list_objs:
            dict_1 = a.to_dictionary()
        with open(cls.__name__ + ".csv", 'w') as mycsv:
            keys = dict_1.keys()
            pepito = csv.DictWriter(mycsv, keys)
            pepito.writeheader()
            pepito.writerow(dict_1)
        


    @classmethod
    def load_from_file_csv(cls):
        juanitolist = []

        with open(cls.__name__ + ".csv", newline='') as mycsv:
            var = csv.DictReader(mycsv)
            for row in var:
                for key, value in row.items():
                    row[key] = int(value)
                juanitolist.append(row)
        return [cls.create(**a) for a in juanitolist]
