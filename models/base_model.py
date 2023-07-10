#!/usr/bin/python3
"""This is the base model for AirBnB"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        args: wont be used
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strftime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Method that return a string
        of class name, id and dictionary"""
        class_name = "[" + self.__class__.name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + "(" + self.id + ")" + str(dct)

    def save(self):
        """Method that updates the attribute updated_at
        with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Creates a dictionary of the class and returns it
        with all key values of __dict__"""
        my_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "upadated_at":
                my_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    my_dict[key] = values
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
