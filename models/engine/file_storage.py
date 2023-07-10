#!/usr/bin/python3
"""This module file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """this class serializes instances to a JSON file and
    deserializes JSON file  to instances
    __file_path: path to athe JSOn file
    __objects: objects  will be stored"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return self.__objects

    def new(self, obj):
        """adds a new object to __objects"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """serializes __object to the JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(my_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects if
        __file_path exist"""
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
