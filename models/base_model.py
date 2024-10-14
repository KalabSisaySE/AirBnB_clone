#!/usr/bin/python3
"""defines the base class BaseModel"""
import copy
from datetime import datetime, timezone
from uuid import uuid4

from models import storage


class BaseModel:
    """represents the common attributes/methods all the other models"""

    def __init__(self, *args, **kwargs):
        """instantiates the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
            storage.new(self)

    def __str__(self):
        """string representation of the model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the `updated_at` time"""
        self.updated_at = datetime.now(timezone.utc)
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        new_dict = copy.deepcopy(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()

        return new_dict
