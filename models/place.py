#!/usr/bin/python3
"""
Module contains the Place part of the Airbnb
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherets BaseModel
    """
    city_id = ""  # It'll be City.id
    user_id = ""  # It'll be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitud = 0.0
    longitude = 0.0
    amenity_ids = [""]  # List of Amenity.id
