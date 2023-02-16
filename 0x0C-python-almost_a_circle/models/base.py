#!/usr/bin/python3
"""A Module of Class Base."""
import json

class Base:
    """A class Base.

    Attributes:
        _nb_object (int): Number of initialized base.
    """
    __nb_object = 0

    def __init__(self, id=None):
        """Inirialization of the class attribute id.

        Args:
            id (int): The identity of the initialized based.
        """
        if id is not None:
            self.id = id

        else:
            __class__.__nb_object += 1
            self.id = __class__.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """This fuction returns a JSON representation of a list of dictionary"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as fjson:
            if list_objs is None:
                fjson.write("[]")
            else:
                list_dic = [o.to_dictionary for o in list_objs
                            fjson.write(__class__.to_json_string(list_dict))
                            fjson.write(list_dic)
