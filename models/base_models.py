#!/usr/bin/python3
"""This is the bsae model for AirBnB"""
import uuid
from datetime import datetime


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Attributes:
        id: unique id generated
        created_at: creation date
        updated_at: updated date"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """method that return a string 
        of class name, id and dictionary"""
        return f"[{self.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """method that updates the attribute updated_at 
        with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a dictionary of the class and returns it
        with all key values of __dict__"""

        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
