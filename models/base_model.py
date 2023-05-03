#!/usr/bin/python3
"""defines the class `BaseModel`"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """a base class that defines all common attributes/methods for other classes"""

    def __init__(self) -> None:
        """instantiates a new `BaseModel` object"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """the string representation of a `BaseModel` object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """updates the public instance attribute `updated_at` with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of __dict__ of 
        the instance with some additional attributes"""
        to_dict = self.__dict__.copy()
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = to_dict['created_at'].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        to_dict['updated_at'] = to_dict['updated_at'].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        return to_dict
