#!/usr/bin/python3
"""The State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)
