#!/usr/bin/python3
"""defines the City model class"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents a city"""

    state_id = ""
    name = ""
