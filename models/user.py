#!/usr/bin/python3
"""defines the User model class"""
from models.base_model import BaseModel


class User(BaseModel):
    """represents a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
