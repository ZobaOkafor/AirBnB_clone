#!/usr/bin/python3
"""The City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City"""
        super().__init__(*args, **kwargs)
