#!/usr/bin/python3
"""
Module containing the User that inherets BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inheriting BaseModel
    """

    email = ""  # Public attribute, should be a string
    password = ""  # Public attribute, should be a string
    first_name = ""  # Public attribute, should be a string
    last_name = ""  # Public attribute, should be a string
