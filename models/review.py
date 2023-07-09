#!/usr/bin/python3
"""
Module that contains Review of Airbnb
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class of that inherets BaseModel
    """
    place_id = ""  # It'll be Place.id
    user_id = ""  # It'll be User.id
    text = ""
