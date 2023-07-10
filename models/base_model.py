#!/usr/bin/python3
"""This is the base model for AirBnB"""

import uuid
from datetime import datetime


class BaseModel:
    """This class will defines all common attributes/methods
    for other  classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        args: wont be used
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        """Method that return a string
        of class name, id and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the attribute updated_at
        with current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Creates a dictionary of the class and returns it
        with all key values of __dict__"""

        # Makes a copy of __dict__
        my_dict = self.__dict__.copy()

        # Adds class to the dictionary
        my_dict["__class__"] = self.__class__.__name__

        # Makes files ISO format
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
