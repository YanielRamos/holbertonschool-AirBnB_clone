#!/usr/bin/python3
"""
Module contains the city part of the Airbnb
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherets BaseModel
    """

    state_id = ""
    name = ""
