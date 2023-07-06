#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                for key, value in json.load(file).items():
                    value = BaseModel(**value)
                    self.__objects[key] = value

        except FileNotFoundError:
            pass
