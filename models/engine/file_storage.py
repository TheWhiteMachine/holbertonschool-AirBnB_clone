#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
import json

"""FileStorage is a file were the function to work with deserialization and
serialization"""


class FileStorage:
    """The class FileStorage which is in charge of the file storage methods"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """A function that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """A function that sets in __objects the obj with key
        <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """A function that serializes __objects to the JSON file
        (path: __file_path)"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """A function that : deserializes the JSON file to
        __objects (only if the JSON file (__file_path) exists ;
        otherwise, does nothing."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
