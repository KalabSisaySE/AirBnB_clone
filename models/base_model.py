#!/usr/bin/python3
"""the `base_model` module defines the class `BaseModel`"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """a base class that defines all common attributes for other classes"""

    def __init__(self) -> None:
        """instantiates a new `BaseModel` object"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """the string representation of a `BaseModel` object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """updates the  attribute `updated_at` with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns a dictionary containing attributes of the object"""
        to_dict = self.__dict__.copy()
        to_dict["__class__"] = self.__class__.__name__
        to_dict["created_at"] = self.__dict__["created_at"].isoformat()
        to_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        return to_dict
