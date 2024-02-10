#!/usr/bin/python3
"""The Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
